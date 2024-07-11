# Use an official Python runtime as a parent image
FROM python:3.12-rc-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container
COPY . /app/

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set environment variables
ENV PYTHONBUFFERED=1
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:5000 --workers=4"

# Make entrypoint.sh executable
RUN chmod +x entrypoint.sh

# Run entrypoint.sh when the container launches
ENTRYPOINT ["./entrypoint.sh"]
