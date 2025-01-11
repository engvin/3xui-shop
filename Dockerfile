FROM python:3.12-slim-bullseye

ENV PYTHONPATH=/

COPY pyproject.toml /
COPY README.md /
RUN pip install poetry && poetry install

COPY ./app /app