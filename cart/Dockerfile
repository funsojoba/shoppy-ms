# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory within the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN apt-get update && apt-get upgrade -y
RUN apt-get -y --no-install-recommends install netcat build-essential cargo libpq-dev

RUN python -m pip install --upgrade pip setuptools \
    && pip install wheel \
    && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5002 available to the world outside this container
EXPOSE 5002

# Define the command to run your application
CMD ["python", "app.py"]
