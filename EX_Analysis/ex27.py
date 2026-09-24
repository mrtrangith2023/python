users = [
    {"name": "An", "age": 25, "score": 85, "active": True, "premium": False, "blocked": False},
    {"name": "Binh", "age": 32, "score": 90, "active": False, "premium": True, "blocked": False},
    {"name": "Nam", "age": 28, "score": 75, "active": True, "premium": False, "blocked": True},
    {"name": "Lan", "age": 35, "score": 95, "active": True, "premium": False, "blocked": False},
    {"name": "Mai", "age": 40, "score": 70, "active": False, "premium": True, "blocked": True},
    {"name": "Hoa", "age": 22, "score": 92, "active": True, "premium": True, "blocked": False},
    {"name": "Tuan", "age": 30, "score": 88, "active": False, "premium": False, "blocked": False}
]

dem = 0

for user in users:
    if user["age"] >= 30 and (user["score"] >= 90 or user["active"]) and (user["premium"] or not user["blocked"]):
        dem += 1

print("Số lượng users thỏa mãn điều kiện là: ", dem)