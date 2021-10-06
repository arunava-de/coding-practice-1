## Not working!!

def increasing(nums):
    n = len(nums)

    if n<3:
        return False 

    i = 0
    j = 1
    k = 2
    
    while True:
        while j<n-1 and nums[i]>=nums[j]:
            j += 1
        
        # Now we get i<j and nums[i]<nums[j]

        if j>=n-1: # j not found for given i 
            i += 1
            j = i+1
            if i>n-3:
                return False 
            continue
        
        # j found for given i 

        k = j+1 

        while k<n and nums[j]>=nums[k]:
            k += 1

        if k>n-1:
            j += 1
            k = 0
            if j>n-2:
                return False 
            else:
                continue

        return True

        

nums = [1,2,3,4,5]
increasing(nums)
    
nums = [5,4,3,2,1]
increasing(nums)

nums = [1,-1,2,-2,3,-3]
increasing(nums)

nums = [2,3]
increasing(nums)

nums = [1,1,1,1,1,1]
increasing(nums)

nums = [20,100,10,12,5,13]
increasing(nums)

nums = [1,5,0,4,1,3]
increasing(nums)