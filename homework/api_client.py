# homework/api_client.py

import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "bedrooms": 3,
    "bathrooms": 2,
    "sqft_living": 1800,
    "sqft_lot": 5000,
    "floors": 1,
    "waterfront": 0,
    "condition": 3,
}

response = requests.post(url, json=data)

print("Respuesta del servidor:", response.json())