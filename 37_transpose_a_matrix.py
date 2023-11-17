# Program to transpose a matrix

mat = [[1, 2, 3], [4, 5, 6]]

matT = [[0, 0], [0, 0], [0, 0]]

for row in range(len(mat)):
    
    for column in range(len(mat[0])):

        matT[column][row] = mat[row][column]
print(matT)