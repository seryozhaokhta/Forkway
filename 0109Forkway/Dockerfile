# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.11-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install "poetry==1.6.1"

# Switch to the app directory
WORKDIR /app

# Copy the content of the local src directory to the working directory
COPY . /app

# Install the project dependencies
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Specify the command to run on container start
CMD ["poetry", "run", "python", "main.py"]
