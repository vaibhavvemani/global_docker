from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="db",  # Use service name from docker-compose
        user="root",
        password="vaibhav",
        database="crudapp"
    )

@app.route("/api/add", methods=["POST"])
def add_products():
    data = request.get_json()
    name = data.get("name")
    price = data.get("price")

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO products (product_name, product_price) VALUES (%s, %s)", (name, price))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({"message": "Product added successfully"}), 200

@app.route("/api/list", methods=["GET"])
def get_products():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(products), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)