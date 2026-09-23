students = [
    {"name": "An", "age": 20, "score": 85},
    {"name": "Binh", "age": 17, "score": 90},
    {"name": "Nam", "age": 22, "score": 70},
    {"name": "Lan", "age": 19, "score": 95},
    {"name": "Mai", "age": 16, "score": 88}
]

dem = 0

for student in students:
    if student["score"] >= 80:
        dem += 1

print("Số lượng sinh viên có điểm từ 80 là:", dem)