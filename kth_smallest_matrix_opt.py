def kth_smallest(matrix, k):
    n = len(matrix)
    if n==1:
        return matrix[0][0]

    low = matrix[0][0]
    high = matrix[n-1][n-1]
    ans = 0

    while low<=high:
        mid = (low+high)//2 # May or may not exist in the matrix
        c = 0
        j = n-1

        for i in range(n):
            if matrix[i][0]<=mid:
                break 
            while matrix[i][j]>mid:
                j -= 1
            c += j+1

        if c<k:
            low = mid+1
        else:
            ans = mid 
            high = mid-1 # To take core of the case that mid is not in the matrix 

    return ans 

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
kth_smallest(matrix, k)

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 4
kth_smallest(matrix, k)
   
    
