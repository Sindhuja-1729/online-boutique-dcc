
from flask import Flask, jsonify, request
import json
from pathlib import Path

app = Flask(__name__)

file_path = Path(__file__).with_name("products.json")

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

products = data["products"]


@app.route("/")
def home():
    return "Online Boutique Product Catalog API"


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):
    for product in products:
        if product["id"].lower() == product_id.lower():
            return jsonify(product)

    return jsonify({"message": "Product not found"}), 404


@app.route("/search", methods=["GET"])
def search_products():
    query = request.args.get("q", "").lower()

    results = [
        product for product in products
        if query in product["name"].lower()
    ]

    return jsonify(results)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "running"})


if __name__ == "__main__":
    app.run(debug=True)
