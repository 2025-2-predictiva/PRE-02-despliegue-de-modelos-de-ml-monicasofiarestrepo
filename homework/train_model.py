import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# 1. Leer datos
df = pd.read_csv("PRE-02-despliegue-de-modelos-de-ml-monicasofiarestrepo/files/input/house_data.csv")

# 2. Features y target
features = [
    "bedrooms",
    "bathrooms",
    "sqft_living",
    "sqft_lot",
    "floors",
    "waterfront",
    "condition",
]
X = df[features]
y = df["price"]

# 3. Entrenar modelo
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)


output_path = os.path.join(os.path.dirname(__file__), "house_predictor.pkl")

with open(output_path, "wb") as f:
    pickle.dump(model, f)

print("Modelo entrenado y guardado en house_predictor.pkl")