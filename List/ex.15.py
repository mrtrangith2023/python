numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count_total_even = 0

for number in numbers:
    if number % 2 == 0:
        count_total_even += number

print("Tổng các số chẵn trong list numbers là: ", count_total_even)