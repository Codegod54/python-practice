# Find Numbers Divisible by Another Number

num = int(input("Enter an number which you want to find if a number is divisible by another number:"))

for i in range(2, num):
    if (num % i) == 0:
        
        print(num, "is divisible by", i)
        break


else:
    print(num, "is not completly divisible by any number.")
