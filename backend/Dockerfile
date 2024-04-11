
FROM python:3.8-slim-buster

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required packages
RUN apt-get update && apt-get install -y sqlite3 && \
    pip install --no-cache-dir python-dotenv bcrypt jwt pymongo

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the server
CMD ["python", "server.py"]
