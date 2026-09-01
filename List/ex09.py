numbers = [1, 2, 3, 4, 5]

new_numbers = numbers.copy()
for i in new_numbers:
    i **= 2
    print(i)

for i in new_numbers:
    i **= 3
    print(i)