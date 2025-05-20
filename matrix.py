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

if(rows==cols):
     print("It is a square matrix.")
     
diagonal_sum=0
for i in range(rows):
        diagonal_sum+=matrix[i][i]
        
print("Sum of diagonal matrix: ", diagonal_sum)