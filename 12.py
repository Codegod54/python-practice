# Program to Check Leap Year
year = int(input("Enter year:"))

rem = year % 4

if rem == 0:
    print("The given year is leap year", year)
else:
    print("The given year is not leap year", year)