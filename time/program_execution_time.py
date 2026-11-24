import time

start = time.perf_counter()

for i in range(10000):
    pass

end = time.perf_counter()

print("Execution time: ", start - end)
