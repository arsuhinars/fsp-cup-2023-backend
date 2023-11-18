
# Base image
FROM python:3.11-slim as base

ARG SERVER_PORT=8000
ENV SERVER_PORT=$SERVER_PORT

WORKDIR /backend

# Install python packages
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv --no-cache-dir --disable-pip-version-check
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE $SERVER_PORT

# Add entrypoint script
ENTRYPOINT [ "bash", "-c", "uvicorn app.main:app --port $SERVER_PORT --host 0.0.0.0 $@", "docker-entrypoint.sh" ]


# Run image
FROM base as run

COPY app/ app/
