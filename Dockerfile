# Use a slim Python image
FROM python:3.12-slim

# Install uv
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy pyproject.toml and install dependencies
COPY pyproject.toml .
COPY uv.lock .
RUN uv sync --frozen

# Copy application code
COPY . .

# Expose port 5000
EXPOSE 5001

# Run the app
CMD ["uv", "run", "gunicorn", "-b", "0.0.0.0:5001", "app:app"]