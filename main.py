'''Here are the rules of leap years:
1. A year may be a leap year if it is evenly divisible by 4.
2. Years that are divisible by 100 (century years such as 1900 or 2000)
cannot be leap years unless they are also divisible by 400.
(For this reason, the years 1700, 1800, and 1900 were not leap years,
but the years 1600 and 2000 were.)'''

def isLeapYear(year):
    if year % 100 != 0 and year % 4 == 0:
        return True
    if year % 100 == 0 and year % 400 == 0:
        return True
    else:
        False

while True:
    try:
        currentYear = int(input("Please enter the year: "))
        if isLeapYear(currentYear):
            print(currentYear, "is a leap year.")
            break
        else:
            print(currentYear, "is not a leap year.")
            break
    except:
        print("Please try again.")

