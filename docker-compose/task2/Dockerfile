# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application file into the working directory
COPY app.py /app/

# Install the necessary dependencies
RUN pip install Flask

# Expose port 3000 for the application
EXPOSE 3000

# Run the application
CMD ["python", "app.py"]
