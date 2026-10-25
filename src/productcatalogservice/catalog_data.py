
import json
from pathlib import Path

def load_products(filename="products.json"):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["products"]

if __name__ == "__main__":
    products = load_products()
    print("Total products:", len(products))
    for product in products:
        print(product["name"], "-", product["priceUsd"]["units"])
