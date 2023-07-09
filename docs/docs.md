# My App Documentation

## Getting Started

This application is a user management system built with a Flask backend, a React frontend, and a MongoDB database. It provides a simple API for creating, reading, updating, and deleting users. The frontend provides a dashboard and a user list page for managing users.

To run this application, you need Docker and Docker Compose. Once you have these installed, navigate to the root directory of this project and run the following command:

```bash
docker-compose up --build
```

This command builds and starts the application. You can then access the application at http://localhost:80 and the API at http://localhost:5000.

## API Endpoints

The API provides the following endpoints:

- `GET /api/users`: Fetch all users. You can add query parameters to this endpoint to filter the users.
- `POST /api/users`: Create a new user. The request body should be a JSON object with the following properties: `name`, `email`, `age`, and `color`.
- `GET /api/users/<id>`: Fetch a single user by their ID.
- `PUT /api/users/<id>`: Update a user by their ID. The request body should be a JSON object with the properties to update.
- `DELETE /api/users/<id>`: Delete a user by their ID.

## User Management

You can manage users through the frontend of the application. Navigate to the dashboard at http://localhost:80. From there, you can click on the "Go to User List" link to view the user list page.

On the user list page, you can see a list of all current users and their details. You can select one or more users and click the "Delete User" button to delete them. To add a new user, click the "Add User" button. To edit a user, select them and click the "Edit User" button.

There is also a search bar on the user list page. You can enter a user's name into the search bar to filter the list of users.
