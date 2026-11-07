
import json
from collections import Counter

with open("products.json", "r", encoding="utf-8") as f:
    data = json.load(f)

products = data["products"]

print("Total products:", len(products))

categories = Counter(
    category
    for product in products
    for category in product.get("categories", [])
)

print("\nProducts by category:")
for category, count in categories.items():
    print(category, ":", count)
