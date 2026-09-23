products = [
    {"name": "Laptop", "price": 2500, "stock": 5, "active": True},
    {"name": "Mouse", "price": 300, "stock": 20, "active": True},
    {"name": "Monitor", "price": 1800, "stock": 0, "active": True},
    {"name": "Keyboard", "price": 800, "stock": 10, "active": False},
    {"name": "Headphone", "price": 1200, "stock": 3, "active": False}
]

dem = 0

for product in products:
    if product["price"] >= 1000 and (product["stock"] > 0 or product["active"] == True):
        dem += 1

print("Số lượng sản phẩm thỏa điều kiện là: ", dem)