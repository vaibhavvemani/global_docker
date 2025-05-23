from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    house_size = request.form.get("area")
    input_data = pd.DataFrame({"size": [float(house_size)]})

    with open("custom_model.pkl", "rb") as f:
        global model 
        model = pickle.load(f)
        
    result = model.predict(input_data)

    return render_template("index.html", prediction=int(result[0]))

if __name__ == "__main__":
    app.run('0.0.0.0', port=8000)   