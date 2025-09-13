# homework/api_server.py

import pickle
import os
from flask import Flask, request, jsonify

# Ruta robusta al archivo del modelo (misma carpeta del script)
model_path = os.path.join(os.path.dirname(__file__), "house_predictor.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    try:
        features = [
            data["bedrooms"],
            data["bathrooms"],
            data["sqft_living"],
            data["sqft_lot"],
            data["floors"],
            data["waterfront"],
            data["condition"],
        ]
        pred = model.predict([features])[0]
        return jsonify({"predicted_price": float(pred)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)