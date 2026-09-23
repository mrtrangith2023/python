students = [
    {"name": "An", "age": 20, "score": 85},
    {"name": "Binh", "age": 17, "score": 90},
    {"name": "Nam", "age": 22, "score": 70},
    {"name": "Lan", "age": 19, "score": 95},
    {"name": "Mai", "age": 16, "score": 88}
]

list_student = []

for student in students:
    if student["age"] >= 18 and student["score"] >= 80:
        list_student.append(student)

print(list_student)