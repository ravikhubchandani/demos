# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy requirements.txt and install dependencies, flask MUST be part of it
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 to the outside world
EXPOSE 80

# Set environment variable for Flask to locate the app
ENV FLASK_APP=main.py

# Run the Flask app, listening on all interfaces at port 80
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
