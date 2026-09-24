users = [
    {"name": "An", "age": 25, "active": True, "blocked": False},
    {"name": "Binh", "age": 32, "active": True, "blocked": True},
    {"name": "Nam", "age": 28, "active": False, "blocked": False},
    {"name": "Lan", "age": 35, "active": True, "blocked": False},
    {"name": "Mai", "age": 22, "active": False, "blocked": True},
    {"name": "Hoa", "age": 40, "active": True, "blocked": False}
]

dem = 0

for user in users:
    if user["age"] >= 30 and user["active"] == True and not user["blocked"]:
        dem += 1

print("Số lượng users thỏa mãn điều kiện là: ", dem)