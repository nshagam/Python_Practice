# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous
# two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fib(n):
    n1 = 1
    n2 = 1

    fibonnaci = [n1, n2]
    for i in range(2, n):
        fibonnaci.append(fibonnaci[i-2] + fibonnaci[i-1])

    return fibonnaci

num = int(input("How many Fibonnaci numbers should be generated? "))

if num == 1:
    print([1])
elif num == 2:
    print([1, 1])
else:
    print(fib(num))


