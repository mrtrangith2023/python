students = [
    {"name": "An", "age": 20, "score": 85, "active": True},
    {"name": "Binh", "age": 17, "score": 92, "active": True},
    {"name": "Nam", "age": 22, "score": 75, "active": False},
    {"name": "Lan", "age": 19, "score": 95, "active": True},
    {"name": "Mai", "age": 21, "score": 88, "active": False},
    {"name": "Hoa", "age": 16, "score": 91, "active": True}
]

dem = 0

for student in students:
    if student["age"] >= 18 and (student["score"] >= 90 or student["active"] == True):
        dem += 1

print("Số lượng sinh viên thỏa điều kiện là:", dem)