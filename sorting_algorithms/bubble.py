import random
import time
from datetime import datetime

fruits = [i for i in range(10)]
random.shuffle(fruits)
print(fruits)

start = time.time()
start_date = datetime.now()
n = 1
is_sorted = True
while n < len(fruits):
    for ind in range(len(fruits)-n):
        if fruits[ind] > fruits[ind+1]:
            is_sorted = False
            fruits[ind], fruits[ind+1] = fruits[ind+1], fruits[ind]
    n += 1

    if is_sorted:
        break

result = time.time() - start
end_date = datetime.now() - start_date
# print(start_date - end_date)

print(fruits)
print(result, end_date)
