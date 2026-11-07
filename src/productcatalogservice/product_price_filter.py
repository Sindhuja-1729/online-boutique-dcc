import json

with open("products.json", "r", encoding="utf-8") as f:
    data = json.load(f)

products = data["products"]

minimum = float(input("Enter minimum price: "))
maximum = float(input("Enter maximum price: "))

found = False

for product in products:
    price = product["priceUsd"]["units"]

    if minimum <= price <= maximum:
        print(product["name"], "-", price)
        found = True

if not found:
    print("No products found in this price range")
