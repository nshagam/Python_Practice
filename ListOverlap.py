# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between
# the lists (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
# 1. Randomly generate two lists to test this
# 2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = []
for i in a:
    if i in b:
        if i not in common:
            common.append(i)
print(common)

# Random part
l1 = random.sample(range(30), 15)
l2 = random.sample(range(30), 20)

print(sorted(l1))
print(sorted(l2))

common2 = []
for i in l1:
    if i in l2:
        if i not in common2:
            common2.append(i)
print(sorted(common2))

# One line part
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common3 = list(set(i for i in a if i in b))

print(common3)