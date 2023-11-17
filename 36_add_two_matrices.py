# Program to add two matrices
x = [[1, 2], [3, 4]]
y = [[5, 6], [7, 8]]

sum = [[0, 0], [0, 0]]

for outerLen in range(len(x)):
    for innerLen in range(len(x[0])):
        sum[outerLen][innerLen] = x[outerLen][innerLen] + y[outerLen][innerLen]

print(sum)
