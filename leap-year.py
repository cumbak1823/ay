# To get year (integer input) from the user
# This is my first explanation
year = int(input("Enter a year: "))
# This comment added by Fatih on his local repository
# This is second added comment line
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
