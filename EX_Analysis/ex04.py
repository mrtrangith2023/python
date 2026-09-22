products = [
    {"name": "Keyboard", "price": 500},
    {"name": "Mouse", "price": 300},
    {"name": "Monitor", "price": 2500},
    {"name": "USB", "price": 150},
    {"name": "Headphone", "price": 1200}
]

list_product = []

for product in products:
    if product["price"] >= 1000:
        list_product.append(product)


print(list_product)