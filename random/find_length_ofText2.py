text = "welcome to python"

count = 0

for i in text:
    if i == " ":
        continue
    count += 1

print(count)
