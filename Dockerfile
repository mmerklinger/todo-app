FROM python:3.11-slim

ENV PIP_ROOT_USER_ACTION=ignore
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /todo_app

# Copy project files
COPY poetry.lock pyproject.toml .
COPY todo_app/ todo_app/

# Install dependencies
RUN apt update && apt install -y gcc libpq-dev libpq5 && apt clean
RUN pip install poetry
RUN poetry install --no-root --without=dev

EXPOSE 8080
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8080", "--error-logfile=-", "--worker-connections=100", "--max-requests=1000", "todo_app:app"]
