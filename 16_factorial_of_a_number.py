# Program to Find the Factorial of a Number
num = int(input("Enter number:"))
for x in range(1, num + 1):
    if num % x == 0:
        print(x, end=' ')