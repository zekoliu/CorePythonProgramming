import random

list_index = random.randint(1, 100)

a = []

for i in range(list_index):
    a.append(random.randint(0, 2**31 -1))

a.sort()

print a