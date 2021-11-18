def search(nums, target):

    n = len(nums)

    if n==1:
        return True if nums[0]==target else False 

    low = 0 
    high = n-1 

    while low<=high:
        mid = (low+high)//2

        if nums[mid]==target:
            return True 
        
        while low<mid and nums[low]==nums[mid]:
            low += 1
        
        if nums[low]<=nums[mid]: # low to mid is sorted
            if target>=nums[low] and target<=nums[mid]:
                high = mid-1
            else:
                low = mid+1 
        else:
            if target<=nums[high] and target>=nums[mid]:
                low = mid+1
            else:
                high = mid-1 

    return False

search([1,2,2,3,4,-5,-3,-2], 2)

search([2,5,6,0,0,1,2],3)

search([1,0,1,1,1], 0)
