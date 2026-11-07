import json

with open("products.json", "r", encoding="utf-8") as f:
    data = json.load(f)

products = data["products"]

search_id = input("Enter product ID: ").lower()

found = False

for product in products:
    if product["id"].lower() == search_id:
        print("\nProduct Details")
        print("ID:", product["id"])
        print("Name:", product["name"])
        print("Description:", product["description"])
        print("Categories:", product["categories"])

        price = product["priceUsd"]
        amount = price["units"] + price.get("nanos", 0) / 1000000000

        print("Price:", price["currencyCode"], amount)
        found = True
        break

if not found:
    print("Product not found")
