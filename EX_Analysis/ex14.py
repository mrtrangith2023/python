products = [
    {"name": "Keyboard", "price": 500, "stock": 10},
    {"name": "Mouse", "price": 300, "stock": 0},
    {"name": "Monitor", "price": 2500, "stock": 5},
    {"name": "USB", "price": 150, "stock": 20},
    {"name": "Headphone", "price": 1200, "stock": 0}
]

dem = 0

for product in products:
    if product["price"] >= 1000 and product["stock"] > 0:
        dem += 1

print("Số lượng sản phẩm trong danh sách thỏa điều kiện là: ", dem)