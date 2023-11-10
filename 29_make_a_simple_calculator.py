def addition():
    sum = first_num + second_num
    print("The sum is:", sum)

def subtraction():
    sub = first_num - second_num
    print("The subtraction is:", sub)

def multiplication():
    mul = first_num * second_num
    print("The multipllication is:", mul)

def division():
    div = first_num / second_num
    print("The division is:", div)
select_number = int(input("Enter 1 to add, 2 to subtract, 3 to multiplication, 4 to divid:"))
first_num = int(input("Enter First Number:"))
second_num = int(input("Enter Second Number:"))

if select_number == 1:
    addition()


elif select_number == 2:
     subtraction()

elif select_number == 3:
    multiplication()

elif select_number == 4:
    division()



