FROM python:3.11-slim

ENV PIP_ROOT_USER_ACTION=ignore
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /todo_app

# Install build system and wsgi service
RUN pip install poetry

# Copy project files
COPY poetry.lock pyproject.toml .
COPY todo_app/ todo_app/

# Install dependencies
RUN poetry install --no-root --without=dev

EXPOSE 8080
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8080", "--error-logfile=-", "--worker-connections=100", "--max-requests=1000", "todo_app:app"]
