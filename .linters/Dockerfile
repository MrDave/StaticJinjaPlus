FROM docker.io/python:3.10.12-alpine

ARG BASE_DIR=/opt/linters

ENV \
    # python
    PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # poetry
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apk add --no-cache poetry

WORKDIR ${BASE_DIR}
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry install --no-ansi
