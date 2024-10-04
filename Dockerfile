# Use an official Python runtime as a parent image
FROM python:3.10

# Install FFmpeg and FFprobe for bot requirements
RUN apt-get update -qq && apt-get install -y ffmpeg

# Set the working directory for the bot
WORKDIR /app

# Copy the contents of the bot directory into the container at /app
COPY ./bot /app

# Install bot dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install chromium --with-deps

# Set the working directory for the web app
WORKDIR /webapp

# Copy the web app's contents into the container at /webapp
COPY ./db /webapp

# Install web app dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports for both applications
EXPOSE 8080  # Bot
EXPOSE 5000  # Web app

# Command to start both services
CMD ["sh", "-c", "python3 /app/main.py & gunicorn --bind 0.0.0.0:5000 main:app"]
