FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .
COPY README.md .

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY src/ src/

RUN poetry install

CMD ["uvicorn", "--app-dir=src", "plant_swap.main:app", "--host", "0.0.0.0", "--port", "8000"]
