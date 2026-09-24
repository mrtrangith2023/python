products = [
    {"name": "Laptop", "price": 2500, "stock": 5, "rating": 4.8, "active": True},
    {"name": "Mouse", "price": 300, "stock": 20, "rating": 4.5, "active": True},
    {"name": "Monitor", "price": 1800, "stock": 0, "rating": 4.7, "active": False},
    {"name": "Keyboard", "price": 800, "stock": 10, "rating": 4.2, "active": True},
    {"name": "Headphone", "price": 1200, "stock": 3, "rating": 4.9, "active": False},
    {"name": "Webcam", "price": 1500, "stock": 0, "rating": 4.6, "active": True},
    {"name": "Tablet", "price": 2200, "stock": 8, "rating": 4.3, "active": True}
]

dem = 0

for product in products:
    if (product["price"] >= 1000 or product["stock"] >= 10) and product["rating"] >= 4.5 and product["active"]:
        dem += 1

print("Số lượng sản phẩm thỏa mãn điều kiện là: ", dem)