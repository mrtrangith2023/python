names = ["leo", "messi", "ronaldo", "tony"]

add_name = input("Nhap ten: ")
names.append(add_name)

print(names)

names.remove("messi")
print(names)

if "ronaldo" in names:
    print("ronaldo co trong list names")