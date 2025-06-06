# Use official Python base image
FROM python:3.11-slim

# Set workdir inside container
WORKDIR /app

# Copy python script to container
COPY print_env.py .

# Command to run your python script
CMD ["python3", "print_env.py"]
