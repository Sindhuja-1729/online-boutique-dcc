import json

with open("products.json", "r", encoding="utf-8") as f:
    data = json.load(f)

products = data["products"]

page_size = 5
total = len(products)

page = int(input("Enter page number: "))

total_pages = (total + page_size - 1) // page_size

if 1 <= page <= total_pages:
    start = (page - 1) * page_size
    end = start + page_size

    print("\nPage:", page)

    for product in products[start:end]:
        print(product["name"])
else:
    print("Invalid page number")

print("Total pages:", total_pages)
