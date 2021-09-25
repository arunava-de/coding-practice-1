def prison_after(cells, n):
    prev = cells 
    curr = [None]*len(cells)
    curr[0] = 0
    curr[-1] = 0

    for _ in range(n):
        for j in range(1,len(cells)-1):
            if prev[j-1]==prev[j+1]:
                curr[j] = 1
            else:
                curr [j] = 0
        prev = curr[::]
    
    return curr 

cells = [0,1,0,1,1,0,0,1]
n = 16
prison_after(cells, n)
        
