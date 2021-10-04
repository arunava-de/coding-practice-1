def get_skyline(buildings):

    n = len(buildings)
    if n==1:
        return [[buildings[0][0],buildings[0][2]], [buildings[0][1],0]]

    buildings.sort(key=lambda x: x[0]) # Sorting by x-coordinate
    buildings.append([buildings[-1][1], buildings[-1][1], 0])

    # Let's merge the intersecting buildings to resolve the widths

    skyline = [] # Stores indices of the skyline
    curr = buildings[0]

    for i in range(1,n):
        b = buildings[i]

        if b[0]>curr[1]: # No intersection
            skyline.append([curr[0], curr[2]])
            skyline.append([curr[1], 0])
            curr = b
        elif b[0]==curr[1]: # We choose higher building  
            curr[1] = max(b[1], curr[1])
        else: # We add current to skyline and update to new current
            skyline.append([curr[0], curr[2]])
            curr = b 

    
