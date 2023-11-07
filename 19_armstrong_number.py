# Program to Check Armstrong Number
num = int(input("Enter number:"))
sum = 0
length = len(str(num))
for digit in str(num):
    power_of_digit = int(digit) ** length
   
    sum = sum + power_of_digit

if sum == num:
    print("The number is armstrong number:", num)
else:
    print("The nuumber isn't armstrong number:", num)
    
    

 





