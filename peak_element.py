def find_peak(nums):
    n = len(nums)
    low = 0 
    high = n-1 

    while low<high:

        mid = (low+high)//2 

        if nums[mid+1]<nums[mid]:
            high = mid 
        else:
            low = mid+1

    return low 

    