# Use an official Python runtime as a parent image
FROM python:3.11-slim as builder

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY src/ src/
COPY tests/ tests/
COPY templates/ templates/
COPY static/ static/

# Transpile Python to JavaScript
RUN set -e && \
    mkdir -p static/js && \
    transcrypt -b -n src/three_app.py && \
    ls -l src/__target__ && \
    cp src/__target__/three_app.js static/js/three_app.js && \
    cp src/__target__/org.transcrypt.__runtime__.js static/js/org.transcrypt.__runtime__.js && \
    ls -l static/js

# Run tests
RUN pytest

# Use a smaller, more secure base image for the final image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the installed packages from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy the application's code from the builder stage
COPY --from=builder /app .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME="World"

# Run main.py when the container launches
CMD ["python", "src/main.py"]
