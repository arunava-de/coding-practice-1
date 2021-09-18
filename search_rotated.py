# Search in a rotated sorted array 

def search(nums, target):
    
    n = len(nums)
    if n==1:
        if nums[0]==target:
            return 0
        return -1 

    low = 0 
    high = n-1
    
    while low<=high:
        mid = (low+high)//2

        if nums[mid]==target:
            return mid
        if nums[low]<=nums[mid]: # This part is sorted
            if target>=nums[low] and target<nums[mid]:
                high = mid-1
            else:
                low = mid+1 
        else: # The part from mid to high is sorted
            if target>nums[mid] and target<=nums[high]:
                low = mid+1
            else:
                high = mid-1
    
    return -1


nums = [4,5,6,7,0,1,2]
target = 0
search(nums, target)

nums = [4,5,6,7,0,1,2]
target = 3
search(nums, target)

nums = [3,1]
target = 2
search(nums, target)

nums = [5,1,2,3,4]
target = 1
search(nums, target)
