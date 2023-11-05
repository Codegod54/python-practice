#  Program to Check Prime Number
num = int(input("Enter number:"))

if num == 1:
    print("The given number is not prime number:", num)
elif num > 1:
    for i in range(2, num):
        rem = num % i
        if rem == 0:
            print("The given number is not prime number:", num)
            break
    else:
        print("The given number is prime number:", num)
else:
    print("The given number is not prime number:", num)