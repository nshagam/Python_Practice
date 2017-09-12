# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.


def divisors(number):
    numrange = range(1, number)
    divisor = []

    if number == 1:
        divisor.append(1)
        return(divisor)
    elif number == 2:
        divisor.append(2)
        return (divisor)
    else:
        for i in numrange:
            if number % i == 0:
                divisor.append(i)
                if len(divisor) > 1:
                    break
        return(divisor)


num = int(input("Enter a number: "))

prime = divisors(num)
if len(prime) == 1:
    print(num, "is prime")
else:
    print(num, "is not prime")