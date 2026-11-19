numbers = [12, 45, 3, 98, 67, 4, 89, 10]

small = numbers[0]


for num in numbers:
    if num < small:
        small = num

print(small)
