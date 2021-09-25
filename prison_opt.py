def next_state(prev):
    curr = [None]*len(prev)
    curr[0] = 0
    curr[-1] = 0

    for j in range(1,len(prev)-1):
        if prev[j-1]==prev[j+1]:
            curr[j] = 1
        else:
            curr [j] = 0
    
    return curr

def prison_after(cells, n):
    state_map = dict()
    # state_map[tuple(cells)] = 0
    cycle_found = False
    # k = 1

    while n>0:
        if not cycle_found:
            key = tuple(cells)
            if key in state_map.keys(): # We've found the cycle
                n = n%(state_map[key]-n) # Length of cycle is state_map[key]-n
                cycle_found = True 
            else:
               state_map[key] = n
            
        if n>0:
            n -= 1
            next = next_state(cells)
            cells = next[::]
    
    return cells

cells = [0,1,0,1,1,0,0,1]
n = 7
prison_after(cells, n)


                

