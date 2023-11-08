# Program to Find the Factors of a Number

num = int(input("Enter number:"))
print("The factors of", num, "are: ", end="")

for x in range(1, num + 1):
    if num % x == 0:
        print(x, end=' ')
        