# Base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential

# install dependencies
COPY requirements.txt run.sh ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt --default-timeout=1000 && chmod +x ./run.sh

# copy project
COPY . .

# Set entrypoint
ENTRYPOINT bash ./run.sh