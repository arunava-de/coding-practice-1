def largest_rectangle_area(heights):
    n = len(heights)
    maxx = 0

    if n==1:
        return heights[0]

    S = [-1]
    heights.append(0)

    for i in range(n+1):
        while heights[S[-1]]>heights[i]:
            h = heights[S.pop()]
            w = i - S[-1] - 1
            maxx = max(maxx, w*h)
        S.append(i)
    
    return maxx 

    