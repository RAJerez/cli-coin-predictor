FROM python:3.10-slim

RUN apt-get update

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

RUN pip install poetry==1.7.1

ENV PYTHONPATH "${PYTHONPATH}:/app/"

WORKDIR /app

COPY ../poetry.lock ./
COPY ../pyproject.toml ./

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "cli/cli.py"]