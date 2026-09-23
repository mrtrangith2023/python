products = [
    {"name": "Laptop", "price": 2500, "stock": 5, "active": True, "rating": 4.8},
    {"name": "Mouse", "price": 300, "stock": 20, "active": True, "rating": 4.5},
    {"name": "Monitor", "price": 1800, "stock": 0, "active": True, "rating": 4.7},
    {"name": "Keyboard", "price": 800, "stock": 10, "active": False, "rating": 4.2},
    {"name": "Headphone", "price": 1200, "stock": 3, "active": False, "rating": 4.9},
    {"name": "Webcam", "price": 1500, "stock": 0, "active": False, "rating": 4.6}
]

dem = 0
list_product = []

for product in products:
    if product["price"] >= 1000 and (product["stock"] > 0 or product["active"] == True) and product["rating"] >= 4.5:
        dem += 1
        list_product.append(product)

print("Số lượng sản phẩm thỏa điều kiện là:", dem)
print(list_product)