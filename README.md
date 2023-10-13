# Todo-App

A web-based todo application.

## Setup Python virtual environment

This project uses Poetry (minimum version `1.2.0`) as its build system.
A working installation of Poetry is a prerequisite.

Following instructions must be run on the terminal.

1. Clone the repository with Git.
2. Change the working directory to the cloned repository.
3. Enter `poetry install` to install required dependencies.
4. Enter `poetry shell` to change to make the shall aware of the virtual environment.
   This command needs to be repeated whenever the terminal is reopened.

## Run Flask

This instructions require the setup from the previous chapter.
To run the Flask development server enter `flask --app todo_app run`.
Appending `--debug` to the command above will start the server in development mode and produce more output for debugging.
