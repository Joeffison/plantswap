FROM curlimages/curl-base:8.11.0 AS poetry-installer

WORKDIR /installer

RUN curl -sSL https://install.python-poetry.org -o /install-poetry.py


FROM python:3.13.0-slim-bookworm AS poetry

ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

ENV POETRY_HOME /usr/bin/poetry
ENV POETRY_NO_INTERACTION 1
ENV POETRY_VIRTUALENVS_IN_PROJECT true

ENV PATH $POETRY_HOME/bin:$PATH
ENV POETRY_VERSION 1.8.4

WORKDIR /installer

RUN --mount=type=bind,source=/install-poetry.py,from=poetry-installer,target=/install-poetry.py \
    python /install-poetry.py


FROM poetry AS build

WORKDIR /app

RUN --mount=type=bind,source=poetry.lock,target=poetry.lock \
#     --mount=type=bind,source=poetry.toml,target=poetry.toml \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    poetry install --no-root --without dev

COPY src ./src
RUN --mount=type=bind,source=poetry.lock,target=poetry.lock \
#     --mount=type=bind,source=poetry.toml,target=poetry.toml \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    poetry install --only-root


FROM python:3.13.0-slim-bookworm AS production

RUN adduser --system app
USER app

# due to ENV POETRY_VIRTUALENVS_IN_PROJECT true in poetry stage
ENV PATH /app/.venv/bin:$PATH

COPY --from=build /app /app
WORKDIR /app
# COPY gunicorn.conf.py gunicorn_logging.conf ./

# checkov:skip=CKV_DOCKER_4:COPY does not work for URLs
# trivy:ignore:AVD-DS-0005
# ADD --chown=app https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem /app/.aws/rds/global-bundle.pem

HEALTHCHECK CMD ["curl", "http://localhost:8080/api/health"]
# CMD ["gunicorn"]

CMD ["uvicorn", "--app-dir=src", "plant_swap.main:app", "--host", "0.0.0.0", "--port", "8000"]
