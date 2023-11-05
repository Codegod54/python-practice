#  Program to Display Powers of 2 Using Anonymous Function
num = int(input("Enter the power you want:"))

map_result = map(lambda i : 2 ** i, range(num))
print("2 to the power up to", num, "is", list(map_result))
