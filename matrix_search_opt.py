def search_matrix(matrix, target):

    m = len(matrix)
    n = len(matrix[0])

    i = m-1
    j = 0

    while i>=0 and j<n:
        if matrix[i][j]>target: # We move one row up since row sorted in ascending order
            i -= 1
        elif matrix[i][j]<target: # We move one col to the right 
            j += 1
        else:
            return True

    return False 