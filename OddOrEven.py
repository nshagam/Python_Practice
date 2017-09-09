# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.


# Extras:

# 1. If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num)
# and one number to divide by (check). If check divides evenly into num,
# tell that to the user. If not, print a different appropriate message.

num = int(input("Enter a number: "))

if num % 2 == 0:
    if num % 4 == 0:
        print(num, "is a multiple of 4")
    else:
        print(num, "is even.")
else:
    print(num, "is odd.")

numerator = int(input("Enter a number: "))
denominator = int(input("Enter another number: "))

if numerator % denominator == 0:
    print(denominator, "divides evenly into", numerator)
else:
    print(denominator, "does not divide evenly into", numerator)