# Use official Python 3.11 image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy test script
COPY test_script.py .

# Default command
CMD ["python", "test_script.py"]
