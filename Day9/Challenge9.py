#Matrix Diagnostics — Given a 3×3 grid, write a function to sum the primary and secondary diagonals.
matrix = [[1,2,3],[4,5,6],[7,8,9]]
centre_row = len(matrix)//2
centre_col = len(matrix[centre_row])//2
centre_element = matrix[centre_row][centre_col]

main_diagonalsum = 0
secondary_diagonalsum = 0

for i in range(len(matrix)):
    main_diagonalsum = main_diagonalsum + matrix[i][i]

for i in range(len(matrix)):
    secondary_diagonalsum = secondary_diagonalsum+matrix[i][len(matrix)-1-i]

finalsum = main_diagonalsum + secondary_diagonalsum-centre_element

print("Final sum: ",finalsum)