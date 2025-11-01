# Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY src/ .

ENV FLASK_APP=main.py

# Command to run the application
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]