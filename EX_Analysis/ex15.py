employees = [
    {"name": "An", "salary": 1500, "experience": 3},
    {"name": "Binh", "salary": 900, "experience": 5},
    {"name": "Nam", "salary": 2000, "experience": 2},
    {"name": "Lan", "salary": 1800, "experience": 4},
    {"name": "Mai", "salary": 1200, "experience": 1}
]

dem = 0

for employee in employees:
    if employee["salary"] >= 1500 or employee["experience"] >= 5:
        dem += 1

print("Số lượng nhân viên thỏa mãn điều kiện là: ", dem)