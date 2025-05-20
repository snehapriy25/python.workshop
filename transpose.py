rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []

print("Enter the elements of the matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix.append(row)

print("The matrix is:")
for row in matrix:
    print(row)


transpose = []
for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    transpose.append(new_row)

print("The transpose matrix is:")
for row in transpose:
    print(row)
