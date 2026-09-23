numbers = [4, 7, 10, 13, 16, 21, 24, 30]

dem = 0

for number in numbers:
    if number % 2 == 0:
        dem += 1

print(dem)