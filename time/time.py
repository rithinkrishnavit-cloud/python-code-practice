import time

# return current time in second
current_time = time.time()
print(current_time)

# Converts a timestamp into a readable date and time
print(time.ctime(current_time))

local = time.localtime()
print(local.tm_hour)
time.sleep(1)
print(local.tm_min)
time.sleep(1)
print(local.tm_sec)
time.sleep(1)

# pause execution time
time.sleep(2)
print("Hello")
