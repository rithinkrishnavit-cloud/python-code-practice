def find_fib(num):

    if num <= 1:
        return num

    return find_fib(num - 1) + find_fib(num - 2)


for i in range(10):
    print(find_fib(i))
