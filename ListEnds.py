# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the
# first and last elements of the given list. For practice, write this code inside a function.

def listconversion(l):
    newlist = []
    newlist.append(l[0])
    newlist.append(l[len(l)-1])

    return(newlist)


a = [5, 10, 15, 20, 25]

print(listconversion(a))
