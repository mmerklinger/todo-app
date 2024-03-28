ARG PYTHON_VERSION=3.11

FROM python:$PYTHON_VERSION-alpine AS build

ENV PIP_ROOT_USER_ACTION=ignore
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /todo_app

# Copy project files
COPY poetry.lock pyproject.toml .
COPY todo_app/ todo_app/

# Install dependencies
RUN apk update && apk add gcc libc-dev libpq-dev && apk cache clean
RUN pip install poetry
RUN poetry install --no-root --without=dev

FROM python:$PYTHON_VERSION-alpine

# Copy project files
COPY poetry.lock pyproject.toml .
COPY todo_app/ todo_app/

# Install dependencies
RUN apk update && apk add libpq && apk cache clean

# Copy build artifacts
COPY --from=build /usr/local /usr/local

EXPOSE 8080
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8080", "--error-logfile=-", "--worker-connections=100", "--max-requests=1000", "todo_app:app"]
