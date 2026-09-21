users = [
    {"name": "An", "age": 40},
    {"name": "Binh", "age": 25},
    {"name": "Nam", "age": 35},
    {"name": "Lan", "age": 20}
]
list_user = []

for user in users:
    if user["age"] >= 30:
        list_user.append(user)

print(list_user)