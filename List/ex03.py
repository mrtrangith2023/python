numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print("Các phần tử có vị trí index chẵn:", number)

for number in numbers:
    if number % 2 != 0:
        print("Các phần tử có vị trí index lẻ:", number)

print(numbers[::-1])