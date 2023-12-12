# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY req.txt .

# Установка ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Install the dependencies
RUN pip install --no-cache-dir -r req.txt

# Copy the entire current directory into the container at /app
COPY . .

# Command to start the FastAPI server using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]