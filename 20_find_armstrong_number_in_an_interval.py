# Program to Find Armstrong Number in an Interval
num = int(input("Enter number:"))
for number in range(0, num):
    sum = 0
    length = len(str(number))
    for digit in str(number):
        power_of_digit = int(digit) ** length
   
        sum = sum + power_of_digit

    if sum == number:
        print("The number is armstrong number:", number)
