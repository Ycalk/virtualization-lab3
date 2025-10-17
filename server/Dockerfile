FROM python:3.12-slim

RUN pip install --no-cache-dir poetry==2.2.1

WORKDIR /app

COPY pyproject.toml .
RUN poetry install --no-root

COPY . .
RUN poetry install

CMD ["poetry", "run", "server"]