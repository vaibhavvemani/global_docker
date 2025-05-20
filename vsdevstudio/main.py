from flask import Flask, request, jsonify

app = Flask(__name__)

DATA = []
@app.route("/api/products", methods=["POST"])
def create_product():
    data = request.get_json()
    DATA.append(data)
    return data.jsonify({"message": "Product created "}, 200)

@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(DATA), 200