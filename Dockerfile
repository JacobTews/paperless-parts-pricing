FROM python:3.11-slim

# Install ODBC dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    gnupg \
    curl \
    unixodbc \
    unixodbc-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start app
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT app:app"]
