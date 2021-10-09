def sortColors(nums):

    colors = dict()
    colors[0] = 0
    colors[1] = 0
    colors[2] = 0
    
    for i in range(len(nums)):
        colors[nums[i]] += 1
        
    c = 0
    
    for i in range(len(nums)):
        while colors[c]==0:
            c += 1
            
        nums[i] = c
        colors[c] -= 1