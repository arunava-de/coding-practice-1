from math import ceil 

def search_matrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    if m==1 and n==1:
        if matrix[0][0]==target:
            return True 
        return False 

    low = 0
    high = m-1

    while low<=high:
        mid = (low+high)//2 
        if target in matrix[mid]:
            return True 
        else:
            if target<matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1
    
    return False 

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
search_matrix(matrix, target)

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
search_matrix(matrix, target)

matrix = [[1,3,5,7,8]]
target = 5
search_matrix(matrix, target)

matrix = [[1],[3],[5],[7],[9]]
target = 5
search_matrix(matrix, target)

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 5
search_matrix(matrix, target)