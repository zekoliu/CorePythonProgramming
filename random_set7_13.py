
import random

one = set()
two = set()

for i in range(10):
    one_element = random.randint(1, 10)
    one.add(one_element)

for i in range(10):
    two_element = random.randint(1, 10)
    two.add(two_element)

print one | two, one & two