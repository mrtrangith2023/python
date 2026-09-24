users = [
    {"name": "An", "age": 25, "active": True, "blocked": False, "premium": True},
    {"name": "Binh", "age": 35, "active": True, "blocked": True, "premium": False},
    {"name": "Nam", "age": 40, "active": False, "blocked": False, "premium": True},
    {"name": "Lan", "age": 32, "active": True, "blocked": False, "premium": False},
    {"name": "Mai", "age": 28, "active": False, "blocked": True, "premium": True},
    {"name": "Hoa", "age": 45, "active": True, "blocked": False, "premium": True}
]

dem = 0

for user in users:
    if user["age"] >= 30 and (user["active"] == True or user["premium"] == True) and not user["blocked"]:
        dem += 1

print("Số lượng users thỏa mãn điều kiện là: ", dem)