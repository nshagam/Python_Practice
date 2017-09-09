import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))
now = datetime.date.today()

if age > 100:
    print("Congrats you are old as shit")
elif age == 100:
    print(now.year)
else:
    age_100 = now.year + (100-age)
    print(name + " will be 100 in the year: " + str(age_100))



