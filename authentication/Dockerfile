FROM python:3.8.0-slim as builder

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get upgrade -y
RUN apt-get -y --no-install-recommends install netcat build-essential cargo libpq-dev

RUN python -m pip install --upgrade pip setuptools \
    && pip install wheel \
    && pip install -r requirements.txt


RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define the command to run your application
CMD ["python", "app.py"]
