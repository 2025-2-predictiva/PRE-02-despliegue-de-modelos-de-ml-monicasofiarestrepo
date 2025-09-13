# homework/web_app.py

import pickle
from flask import Flask, render_template_string, request

# 1. Cargar modelo
with open("homework/house_predictor.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

# 2. Plantilla inline sencilla
form_html = """
<!DOCTYPE html>
<html>
  <head><title>House Price Predictor</title></head>
  <body>
    <h2>House Price Predictor</h2>
    <form method="POST" action="/">
      Bedrooms: <input name="bedrooms"><br>
      Bathrooms: <input name="bathrooms"><br>
      Sqft Living: <input name="sqft_living"><br>
      Sqft Lot: <input name="sqft_lot"><br>
      Floors: <input name="floors"><br>
      Waterfront (0/1): <input name="waterfront"><br>
      Condition (1-5): <input name="condition"><br>
      <input type="submit" value="Predict">
    </form>
    {% if prediction %}
      <h3>Predicted Price: {{ prediction }}</h3>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def predict_form():
    prediction = None
    if request.method == "POST":
        features = [
            float(request.form["bedrooms"]),
            float(request.form["bathrooms"]),
            float(request.form["sqft_living"]),
            float(request.form["sqft_lot"]),
            float(request.form["floors"]),
            float(request.form["waterfront"]),
            float(request.form["condition"]),
        ]
        prediction = model.predict([features])[0]
        prediction = round(prediction, 2)
    return render_template_string(form_html, prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)