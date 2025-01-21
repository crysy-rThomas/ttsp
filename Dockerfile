# Stage 1: Build Stage
FROM python:3.11.5 AS base

# Install system packages required for creating virtual environment
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Create a new user
RUN useradd -m myuser

# Set working directory
WORKDIR /code

# Copy requirements files
COPY requirements.txt /code/requirements.txt

# Stage 2: Development Stage
FROM base AS dev

# Create and activate virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install development requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy application code
COPY ./app /code/app
WORKDIR /code/app

# Switch to the new user
USER myuser

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://host.docker.internal:8001 || exit 1

# Run server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
