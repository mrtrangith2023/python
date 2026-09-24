employees = [
    {"name": "An", "age": 25, "salary": 1500, "active": True, "blocked": False},
    {"name": "Binh", "age": 35, "salary": 2000, "active": True, "blocked": True},
    {"name": "Nam", "age": 40, "salary": 1200, "active": False, "blocked": False},
    {"name": "Lan", "age": 32, "salary": 1800, "active": True, "blocked": False},
    {"name": "Mai", "age": 28, "salary": 2500, "active": True, "blocked": False},
    {"name": "Hoa", "age": 45, "salary": 3000, "active": False, "blocked": False}
]

dem = 0

for employee in employees:
    if employee["age"] >= 30 and (employee["salary"] >= 1800 or employee["active"] == True) and not employee["blocked"]:
        dem += 1

print("Số lượng nhân viên thỏa điều kiện là: ", dem)