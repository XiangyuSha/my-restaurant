# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port your app runs on
EXPOSE 8080

# Command to run your app
CMD ["python", "app.py"]
