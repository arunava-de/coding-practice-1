def bsearch(matrix, r, target):
        
    s = 0
    e = len(matrix[0])-1
    
    while s<=e:
        mid = (s+e)//2
        
        if matrix[r][mid]==target:
            return True 
        elif matrix[r][mid]<target:
            s = mid+1
        else:
            e = mid-1
            
    return False

def searchMatrix(matrix, target):
    
    n = len(matrix)
    
    for r in range(n):
        if bsearch(matrix, r, target):
            return True 
        
    return False