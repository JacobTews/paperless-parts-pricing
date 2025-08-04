import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from a containerized Python app!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Railway-provided port or fallback to 5000
    app.run(host="0.0.0.0", port=port)
