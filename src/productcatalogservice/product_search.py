
import json

with open("products.json", "r", encoding="utf-8") as f:
    data = json.load(f)

products = data["products"]

search_name = input("Enter product name: ").lower()

found = False

for product in products:
    if search_name in product["name"].lower():
        print("\nProduct:", product["name"])
        print("Description:", product["description"])
        print("Categories:", product["categories"])
        found = True

if not found:
    print("Product not found")
