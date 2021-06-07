# Elena Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.
![image](https://user-images.githubusercontent.com/60936890/121037386-0857b980-c775-11eb-81a4-c0b990d9fc02.png)

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

## Tasks

There are `@TODO` comments throughout the project. We recommend tackling the sections in order. Start by reading the READMEs in:

1. [`./backend/`](./backend/README.md)
2. [`./frontend/`](./frontend/README.md)

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask server with a pre-written SQLAlchemy module to simplify your data needs. You will need to complete the required endpoints, configure, and integrate Auth0 for authentication.

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The `./frontend` directory contains a complete Ionic frontend to consume the data from the Flask server. You will only need to update the environment variables found within (./frontend/src/environment/environment.ts) to reflect the Auth0 configuration details set up for the backend app.

[View the README.md within ./frontend for more details.](./frontend/README.md)

### Barista JWT
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkFhWXRQSXBsbEJGWVhlQ3ZJbTlmbiJ9.eyJpc3MiOiJodHRwczovL2Rldi1lbGMudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwYWMwNzZlYjIwMGM0MDA3MTE2ZmYzMiIsImF1ZCI6ImNvZmZlZXNob3AiLCJpYXQiOjE2MjMwNzU2MTgsImV4cCI6MTYyMzA4MjgxOCwiYXpwIjoiVklnZTB3S21WcFBSa3k5Y1FYOGpwWThPS0tVTk5FbHAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpkcmlua3MtZGV0YWlsIl19.itaLCbuayHUqQzyXQxfhwYviIjSAiBsJelZhHu30KgSVMFbCspBf6nfSOvaSkxG_0VnDKNBDaDw3hgAA-yexLeAerA23iODPpQ5kS0y50Rs4v7-0wj2kBxQrHLsoSmNK0Oqq4DtDK57v8BIE0fQ1lwxI5JOrbzHvU6Mx1U1NBStN3Hb4A7K72Agn-d-H4KkgAH2Egy4bzgBgmbQoOOg2mczWs_55pNC9kNOQnlsG4FqeExQoPTOpHVmjdV5APSNKwodApcNdwn17cJL68bq2dWVP2zRCwKcktJSh7JxH1PK7R0vy86WfTNDtUdUsVugZADXWe2upoVZLids138o-PQ

### Manager JWT
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkFhWXRQSXBsbEJGWVhlQ3ZJbTlmbiJ9.eyJpc3MiOiJodHRwczovL2Rldi1lbGMudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwYWQ1MmFjYzY1OWFjMDA2ODJmMjNmYSIsImF1ZCI6ImNvZmZlZXNob3AiLCJpYXQiOjE2MjMwNzUzNjAsImV4cCI6MTYyMzA4MjU2MCwiYXpwIjoiVklnZTB3S21WcFBSa3k5Y1FYOGpwWThPS0tVTk5FbHAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpkcmlua3MiLCJnZXQ6ZHJpbmtzLWRldGFpbCIsInBhdGNoOmRyaW5rcyIsInBvc3Q6ZHJpbmtzIl19.jpkc1JNwPD7pbNxpO5nv_sS8l_KpXWXRt_kFQpYEY9w05GZFBh4v0EdwHPIhzMr2qAaA2aS8GJ8bZrSR9pU4mWvglOZzTSXdmopJy6GirGmh49falIANkQy5pNgtFQzT24hNSd5TjcQ1oYb8c1OoORG90_n20KGzSwzcF4vaTUVACXyRILYX1ekxDPRS3DgQ1tONDp3V32cy2cdHEyNcDhnGdbj1zRkX5XF4u_M6sN7sqGsSmo-oqDo1MCuQxb86bCNRX7GzJTV3vpAHF7KjfidX-4Wh40ulEz9s9eULbGywW-JJWOuSFgEKCEtmEjaPyXeUZWjLWr0AB64TfYptFw
