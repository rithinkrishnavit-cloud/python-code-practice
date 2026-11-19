numbers = [12, 45, 23, 67, 34, 89, 10]

first = 0
second = 0

for num in numbers:
    if num > first:
        second = first
        first = num

print(second)
