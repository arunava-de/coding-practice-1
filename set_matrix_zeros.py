def set_zero_row(r, matrix, n):
    for j in range(n):
        if matrix[r][j]=='*':
            continue
        matrix[r][j] = 0

def set_zero_col(c, matrix, m):
    for i in range(m):
        if matrix[i][c]=='*':
            continue
        matrix[i][c] = 0

def set_zeroes(matrix):

    # Let's mark all 0s with another symbol for now

    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = '*'

    for i in range(m):
        for j in range(n):
            if matrix[i][j]=='*':
                set_zero_row(i, matrix, n)
                set_zero_col(j, matrix, m)

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '*':
                matrix[i][j] = 0
    
    
matrix = [[1,1,1],[1,0,1],[1,1,1]]
set_zeroes(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_zeroes(matrix)