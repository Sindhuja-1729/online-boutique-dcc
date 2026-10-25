
import json

with open("products.json", "r", encoding="utf-8") as f:
    data = json.load(f)

products = data["products"]

print("Total products:", len(products))
print("First product:", products[0]["name"])
print("Catalog loaded successfully")
