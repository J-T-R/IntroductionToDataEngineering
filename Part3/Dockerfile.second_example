FROM python:3.7

ENV POETRY_VERSION=1.1.6

RUN python -m pip install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY second_example.py /app/

ENTRYPOINT ["python", "second_example.py"]