# Use binary search on the range [1,n]

def find_dup(nums):
    n = len(nums)

    if n==2:
        return nums[0]

    low = 1 
    high = n 

    while low<=high:
        mid = (low+high)//2 
        count = 0 

        count = sum(num<=mid for num in nums)

        if count>mid: # Duplicate is on the left 
            dup = mid 
            high = mid-1 
        else:
            low = mid+1 

    return dup
