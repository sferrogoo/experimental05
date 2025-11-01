# Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install pytest

ENV PATH="/root/.local/bin:${PATH}"

# Copy the application code
COPY src/ ./src

# Compile transcrypt files
RUN transcrypt -b -n src/hello.py
RUN mkdir -p static/js && mv src/__target__/* static/js/

COPY templates/ ./templates
COPY tests/ ./tests

# Run tests
RUN pytest

ENV FLASK_APP=src/main.py

# Command to run the application
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]