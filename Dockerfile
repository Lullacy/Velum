# Use the latest Python image from the Python package index
FROM python:3.14

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash appuser

# Ensure we don't generate .pyc files and enable stdout/stderr buffering
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install uv for fast dependency management
RUN pip install --no-cache-dir uv

# Set work directory
WORKDIR /app

# Install dependencies first (layer caching)
COPY pyproject.toml uv.lock ./

# Install dependencies with uv
RUN uv sync --frozen --no-dev

# Copy project files with correct ownership
COPY --chown=appuser:appuser . .

# Switch to non-root user. DO NOT RUN AS ROOT for SECURITY REASONS and do not TOUCH!
USER appuser

# Expose the port the app runs on. This will be connected to Frontend for Otto 
EXPOSE 8000
