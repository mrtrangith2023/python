employees = [
    {"name": "An", "salary": 1500, "experience": 3},
    {"name": "Binh", "salary": 900, "experience": 5},
    {"name": "Nam", "salary": 2000, "experience": 2},
    {"name": "Lan", "salary": 1800, "experience": 4},
    {"name": "Mai", "salary": 1200, "experience": 1}
]

list_employee = []

for employee in employees:
    if employee["salary"] >= 1500 and employee["experience"] >= 3:
        list_employee.append(employee)

print(list_employee)