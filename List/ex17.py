numbers = [8, 2, 9, 11, 4, 1]

max_values = numbers[0]
list_new_number = []

for number in numbers:
    if number > max_values:
        max_values = number
        list_new_number.append(number)


print(list_new_number)