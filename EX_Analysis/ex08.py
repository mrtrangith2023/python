products = [
    {"name": "Keyboard", "price": 500, "stock": 10},
    {"name": "Mouse", "price": 300, "stock": 0},
    {"name": "Monitor", "price": 2500, "stock": 5},
    {"name": "USB", "price": 150, "stock": 20},
    {"name": "Headphone", "price": 1200, "stock": 0}
]

list_product = []

for product in products:
    if (product["stock"] > 0 and (product["price"] >= 2000 or product["stock"] >= 20)):
        list_product.append(product)

print(list_product)