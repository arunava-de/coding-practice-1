def increasing(nums):
    n = len(nums)

    if n<3:
        return False 

    smaller = [-1]*n # Stores index of number < nums[i] and on the left
    greater = [-1]*n # Stores index of number > nums[i] and on the right

    min = 0
    max = n-1

    for i in range(1,n):
        if nums[i]<nums[min]:
            min = i
        elif nums[i]==nums[min]:
            continue
        else:
            smaller[i] = min
    
    for i in range(n-2,-1,-1):
        if nums[i]>nums[max]:
            max = i 
        elif nums[i]==nums[max]:
            continue
        else:
            greater[i] = max 

    for i in range(n):
        if smaller[i]!=-1 and greater[i]!=-1:
            return True 

    return False

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

nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
increasing(nums)