# Program to Check if a Number is Odd or Even

num = int(input("Enter a number:"))

rem = num % 2

if rem == 0:
    print("The given number is even:", num)
else:
    print("The given number is odd:", num)
