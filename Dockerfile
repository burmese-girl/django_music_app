# Use an official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt update && apt install -y postgresql-client

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
