ENV PYTHONUNBUFFERED=1

# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Flask/Gunicorn will run on
EXPOSE 5000

# Run the application using Gunicorn
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
CMD ["python", "-c", "from waitress import serve; from app import app; serve(app, host='0.0.0.0', port=5000)"]
