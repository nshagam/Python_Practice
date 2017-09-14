# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
# list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def dupRemove(l):
    unique = list(set(l))
    return unique

def dupRemoveLoop(l):
    unique = []
    for i in range(0, len(l)):
        if l[i] not in unique:
            unique.append(l[i])
    return unique

test = [1, 1, 1, 3, 4, 4, 6]

print(dupRemove(test))
print(dupRemoveLoop(test))