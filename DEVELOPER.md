# Developer Guide

This guide provides an overview of the project and instructions on how to develop and contribute.

## Project Structure

This project consists of a Flask backend, a React frontend, and a MongoDB database. The application provides a user management system with a simple API for creating, reading, updating, and deleting users.

The project directory structure is as follows:

\```plaintext
/my-app
├── backend
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   ├── setup.py
│   └── tests
├── frontend
│   ├── Dockerfile
│   ├── package.json
│   ├── src
│   └── public
├── nginx
│   ├── Dockerfile
│   └── nginx.conf
├── docs
│   ├── Dockerfile.docs
│   └── docs.md
├── docker-compose.yml
└── .github
    └── workflows
        └── ci.yml
\```

## Building and Running the Project

To build and run the project, you need Docker and Docker Compose installed on your system.

To build and start the application, navigate to the root directory of the project and run the following command:

\```bash
docker-compose up --build
\```

This command builds the Docker images for the backend, frontend, Nginx, and documentation, and starts the containers. You can then access the application at http://localhost:80, the API at http://localhost:5000, and the documentation at http://localhost/docs.

## Development Workflow

This project uses GitHub for version control and collaboration. Here's a typical workflow for making changes and contributing to the project:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your changes: `git checkout -b my-feature-branch`.
4. Make your changes and commit them: `git commit -am "Add some feature"`.
5. Push your changes to GitHub: `git push origin my-feature-branch`.
6. Open a pull request from your feature branch to the original repository.

Before opening a pull request, make sure your changes pass all tests and lint checks. You can run tests and lint checks for the backend with the following commands:

\```bash
# Run tests
docker-compose run backend pytest

# Run lint checks
docker-compose run backend flake8
docker-compose run backend pylint
docker-compose run backend black --check
\```

For the frontend, you can run tests with the following command:

\```bash
docker-compose run frontend npm test
\```

When you open a pull request, the continuous integration pipeline will automatically run the tests and lint checks again.

Happy coding!
