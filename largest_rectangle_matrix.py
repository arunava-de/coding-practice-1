def largest_rectangle(matrix):
    n = len(matrix)
    m = len(matrix[0])

    if n==0 or m==0:
        return 0 

    maxx = 0
    heights = [0]*(m+1)

    for i in range(n):
        for j in range(m):
            heights[j] = heights[j]+1 if matrix[i][j]=='1' else 0 
        S = [-1]

        for j in range(m+1):
            while heights[j]<heights[S[-1]]:
                h = heights[S.pop()]
                w = j - S[-1] - 1
                maxx = max(maxx, h*w)
            S.append(j)

    return maxx 

