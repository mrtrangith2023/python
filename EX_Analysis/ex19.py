employees = [
    {"name": "An", "salary": 1500, "experience": 3, "active": True},
    {"name": "Binh", "salary": 900, "experience": 5, "active": True},
    {"name": "Nam", "salary": 2000, "experience": 2, "active": False},
    {"name": "Lan", "salary": 1800, "experience": 4, "active": True},
    {"name": "Mai", "salary": 1200, "experience": 1, "active": False},
    {"name": "Hoa", "salary": 2500, "experience": 6, "active": False}
]

dem = 0

for employee in employees:
    if employee["salary"] >= 1500 and (employee["experience"] >= 5 or employee["active"] == True):
        dem += 1

print("Số lượng nhân viên thỏa điều kiện là:", dem)