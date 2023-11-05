# Program to Print all Prime Numbers in an Interval
num = int(input("Enter Number:"))

for i in range(1, num +1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print("Prime number is:", i)