# Todo-App

A web-based todo application.

## Development

### Setup Python virtual environment

This project uses Poetry (minimum version `1.2.0`) as its build system.
A working installation of Poetry is a prerequisite.

Following instructions must be run on the terminal.

1. Clone the repository with Git.
2. Change the working directory to the cloned repository.
3. Enter `poetry install` to install required dependencies.
4. Enter `poetry shell` to change to make the shall aware of the virtual environment.
   This command needs to be repeated whenever the terminal is reopened.

### Run Flask

This instructions require the setup from the previous chapter.
To run the Flask development server enter `flask --app todo_app run`.
Appending `--debug` to the command above will start the server in development mode and produce more output for debugging.

During development the service can be configured by specifiying the configuration in a `.env` file in the project root.
For the deployment in a production environment it's recommended to configure them as environment variables.
A minimum configuration consists of the configuration keys `FLASK_SECRET_KEY` and `FLASK_SERVER_NAME`.
The documentation of [Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/#sessions) describes how to generate a good secret key.
More information about the possible configuration keys and values are available in the documentation of [Flask](https://flask.palletsprojects.com/en/3.0.x/config/#builtin-configuration-values) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/config/#configuration-keys).

### Build container

The container can be build from the repository.
To build the container a Docker or Podman installation is required.
The build can be started with `podman build --no-cache -t localhost/todo-app .`.

Alternatively to the local built container, the [Github container registry](https://github.com/mmerklinger/todo-app/pkgs/container/todo-app) provides pre-built images for the releases.