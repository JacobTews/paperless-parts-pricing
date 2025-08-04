FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install flask gunicorn

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT app:app"]
