# This week’s exercise is going to be revisiting an old exercise (see Exercise 5),
# except require the solution in a different way.
#
# Take two lists, say for example these two:
#
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between
# the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extra:
#
# Randomly generate two lists to test this

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

combine = list(set(i for i in a if i in b))

print(combine)

# Extra
rand1 = random.sample(range(30), 15)
rand2 = random.sample(range(30), 20)

combine2 = list(set(i for i in rand1 if i in rand2))
print(combine2)
