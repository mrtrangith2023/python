products = [
    {"name": "Laptop", "price": 2500, "active": True, "blocked": False},
    {"name": "Mouse", "price": 300, "active": True, "blocked": False},
    {"name": "Monitor", "price": 1800, "active": False, "blocked": False},
    {"name": "Keyboard", "price": 800, "active": True, "blocked": True},
    {"name": "Headphone", "price": 1200, "active": False, "blocked": True},
    {"name": "Webcam", "price": 1500, "active": True, "blocked": False}
]

dem = 0

for product in products:
    if product["price"] >= 1000 and (product["active"] == True or not product["blocked"]):
        dem += 1

print("Số lưởng sản phẩm thỏa mãn điều kiện là:", dem)