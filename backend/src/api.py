import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS


from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)


# db_drop_and_create_all()

# ROUTES

# Get drinks
@app.route('/drinks', methods=['GET'])
def get_drinks():
    drinks = Drink.query.all()

    if len(drinks) == 0:
        abort(404)

    formatted_drinks = [drink.long() for drink in drinks]
    return jsonify({
        'success': True,
        'drinks': formatted_drinks
    }), 200

# Get drink-detail


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drink_detail(payload):
    drinks = Drink.query.all()

    if len(drinks) == 0:
        abort(404)

    return jsonify({
        'success': True,
        'drinks': [drink.long() for drink in drinks]
    }), 200

# Add drink


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def add_drink(payload):
    #recipe='[{"name": "water", "color": "blue", "parts": 1}]'
    body = request.get_json()
    title = body.get('title', None)
    recipe = body.get('recipe', None)

    try:
        # adding the new drink to the database
        new_drink = Drink(
            title=title,
            recipe=json.dumps(recipe))
        Drink.insert(new_drink)

        return jsonify({
            'success': True,
            'drinks': [new_drink.long()]}), 200

    except Exception as e:
        print(e)
        abort(422)


@app.route("/drinks/<int:id>", methods=["PATCH"])
@requires_auth('patch:drinks')
def update_drinks(payload, id):

    drink = Drink.query.filter(Drink.id == id).one_or_none()
    if drink == None:
        abort(404)

    body = request.get_json()
    title = body.get('title', None)
    recipe = body.get('recipe', None)
    try:
        drink.title = title
        drink.recipe = json.dumps(recipe)
        drink.update()

        return jsonify({
            'success': True,
            'drinks': [drink.long()]}), 200

    except Exception as e:
        print(e)
        abort(422)


@app.route("/drinks/<int:id>", methods=["DELETE"])
@requires_auth('delete:drinks')
def delete_drink(payload, id):
    drink = Drink.query.filter(Drink.id == id).one_or_none()
    if drink == None:
        abort(404)
    print(drink)
    try:
        drink.delete()
        return jsonify({
            'success': True,
            'delete': id
        }), 200

    except Exception as e:
        print(e)
        abort(422)


# Error Handling
@app.errorhandler(AuthError)
def autherror(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error
    }), error.status_code
