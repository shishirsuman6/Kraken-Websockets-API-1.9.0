# Dockerfile: Blueprint for building images
FROM python:3.9.9

WORKDIR /Kraken-Websockets-API-1.9.0

# RUN pip list --format=freeze > requirements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m", "pytest"]

# Notes/Comments:

# Image: Template for running Containers
# Run this on the terminal to build image: docker build -t pytest-kraken-ws .

# Container: Actual running process where we have our package
# Run this on the terminal to start the container: docker run pytest-kraken-ws