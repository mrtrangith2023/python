numbers = [12, 32, 100, 9, 40]

min_value = numbers[0]

for number in numbers:
    if number < min_value:
        min_value = number

print("Giá trị nhỏ nhất trong list numbers là: ", min_value)