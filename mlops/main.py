from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["POST"])
def home():
    data = request.get_json()
    house_size = data.get("house_size")
    house_size = np.array(int(house_size)).reshape(-1, 1)

    with open("custom_model.pkl", "rb") as f:
        global model 
        model = pickle.load(f)
        
    result = model.predict(house_size)

    return jsonify({ "message": result[0].item()})

if __name__ == "__main__":
    app.run('0.0.0.0', port=8000)   