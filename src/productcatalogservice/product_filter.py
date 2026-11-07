
import json

with open("products.json", "r", encoding="utf-8") as f:
    data = json.load(f)

products = data["products"]

category = input("Enter category: ").lower()

found = False

for product in products:
    if category in product.get("categories", []):
        print(product["name"])
        found = True

if not found:
    print("No products found in this category")
