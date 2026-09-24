employees = [
    {"name": "An", "age": 25, "salary": 1500, "experience": 3, "active": True},
    {"name": "Binh", "age": 35, "salary": 2000, "experience": 6, "active": False},
    {"name": "Nam", "age": 40, "salary": 1200, "experience": 8, "active": True},
    {"name": "Lan", "age": 32, "salary": 1800, "experience": 4, "active": True},
    {"name": "Mai", "age": 28, "salary": 2500, "experience": 2, "active": False},
    {"name": "Hoa", "age": 45, "salary": 3000, "experience": 10, "active": True},
    {"name": "Tuan", "age": 30, "salary": 1400, "experience": 5, "active": False}
]

dem = 0

for employee in employees:
    if (employee["salary"] >= 1800 and employee["experience"] >= 5) or (employee["age"] >= 30 and employee["active"]):
        dem += 1

print("Số lượng nhân viên thỏa mãn điều kiện là: ", dem)