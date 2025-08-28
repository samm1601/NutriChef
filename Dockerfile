# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Prevent Python from writing .pyc files & enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
# Copy and install dependencies
COPY NutriChef/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY NutriChef/ ./NutriChef/

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI app using uvicorn
# NOTE: `NutriChef.api:app` means module NutriChef/api.py, variable app
CMD ["uvicorn", "NutriChef.api:app", "--host", "0.0.0.0", "--port", "8000"]
