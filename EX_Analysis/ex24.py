products = [
    {"name": "Laptop", "price": 2500, "stock": 5, "active": True},
    {"name": "Mouse", "price": 300, "stock": 20, "active": True},
    {"name": "Monitor", "price": 1800, "stock": 0, "active": False},
    {"name": "Keyboard", "price": 800, "stock": 10, "active": True},
    {"name": "Headphone", "price": 1200, "stock": 3, "active": False},
    {"name": "Webcam", "price": 1500, "stock": 0, "active": True}
]

dem = 0

for product in products:
    if (product["price"] >= 1000 or product["stock"] >= 10) and product["active"]:
        dem += 1

print("Số lượng sản phẩm thỏa điều kiện là: ", dem)