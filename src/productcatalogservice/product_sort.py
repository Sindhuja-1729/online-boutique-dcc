import json

with open("products.json", "r", encoding="utf-8") as f:
    data = json.load(f)

products = data["products"]

products.sort(key=lambda p: p["priceUsd"]["units"])

print("Products sorted by price:")

for product in products:
    print(product["name"], "-", product["priceUsd"]["units"])
