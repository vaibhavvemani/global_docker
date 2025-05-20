from flask import Flask, request, jsonify

app = Flask(__name__)
products = []

@app.route("/api/products", methods=["POST"])
def add_products():
    data = request.get_json()
    name = data.get("name")
    price = data.get("price")

    products.append({
        "name": name,
        "price": price
    })

    return jsonify({
        "message": "Product added successfully"
    }, 200)

@app.route("/api/list", methods=["GET"])
def get_products():
    return jsonify(products, 200)

@app.route("/api/clear", methods=["DELETE"])
def clear_products():
    products.clear()
    return jsonify({
        "message": "Products cleared successfully"
    }, 200)

@app.route("/api/update", methods=["PUT"])
def update_product():
    data = request.get_json()
    name = data.get("name")
    price = data.get("price")

    for product in products:
        if product["name"] == name:
            product["price"] = price
            return jsonify({
                "message": "Product updated successfully"
            }, 200)

    return jsonify({
        "message": "Product not found"
    }, 404)

@app.route("/api/delete", methods=["DELETE"])
def delete_product():
    data = request.get_json()
    name = data.get("name")

    for product in products:
        if product["name"] == name:
            products.remove(product)
            return jsonify({
                "message": "Product deleted successfully"
            }, 200)

    return jsonify({
        "message": "Product not found"
    }, 404)

if __name__ == "__main__":
    app.run(port = 8080, host = "0.0.0.0")