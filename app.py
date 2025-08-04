from flask import Flask, request, jsonify
from pricing_module import main

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run_script():
    data = request.get_json()
    input_value = data.get("input")

    if input_value is None or not isinstance(input_value, int):
        return jsonify({"error": "Missing or invalid 'input' (must be an integer)"}), 400

    try:
        result = main(input_value)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
