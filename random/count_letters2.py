text = "hello world"

count = 0

for i in text:
    if text == " ":
        count = -1
    else:
        count += 1

print(count)
