# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

inputStr = str(input("Enter a string: "))
palindrome = True
backwards = ""

i = len(inputStr) - 1
while i >= 0:
    backwards += inputStr[i]
    i -= 1

for i in range(0, len(inputStr), 1):
    if inputStr[i] != backwards[i]:
        palindrome = False

if palindrome == True:
    print(inputStr, "is a palindrome.")
else:
    print(inputStr, "is not a palindrome.")


