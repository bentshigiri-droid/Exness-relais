import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "online", "message": "Relais Exness actif"})


@app.route("/execute", methods=["POST"])
def execute():
    data = request.get_json(force=True)
    action = data.get("action")
    volume = data.get("volume")
    print(f"⚡ Signal reçu : {action} - Lot {volume}")
    return jsonify(
        {"status": "success", "message": f"Ordre {action} {volume} transmis"}
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
