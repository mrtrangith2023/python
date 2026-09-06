numbers = [1, 2, 3, 4, 5, 6, 7]

count_odd = 0

# for number in numbers:
#     if number % 2 == 0:
#         count_even += 1

# print("Số lượng số chẵn trong list numbers là: ", count_even)

for number in numbers:
    if number % 2 != 0:
        count_odd += 1

print("Số lượng số lẻ trong list numbers là: ", count_odd)