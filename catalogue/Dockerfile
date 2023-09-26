# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory within the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Define the command to run your application
CMD ["python", "app.py"]
