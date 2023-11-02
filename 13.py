# Program to Find the Largest Among Three Numbers
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a > b > c:
    print("First number is greater:", a)
elif a < b > c:
    print("Second number is greater:", b)
else:
    print("Third number is greater:", c)