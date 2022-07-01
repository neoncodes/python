import random
import time

list = []
startTime = time.time()
for x in range(1000000000):
    list.append(random.randint(0,9))

endTime = time.time()

print(list)

print(startTime)
print(endTime)