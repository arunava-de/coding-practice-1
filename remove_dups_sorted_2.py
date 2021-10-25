def remove_dups(nums):
    n = len(nums)
    if n<=2:
        return nums 

    left = 0 # Points to unique elements
    right = 0 # Points to last occurence of each unique element
    last = 0

    while right<n:
        curr = nums[left]
 
        while right<n and left<n and nums[right]==curr:
            right += 1

        occs = right-left # Stores occurences
        occs = min(occs, 2)

        for _ in range(0, occs):
            nums[last] = nums[left]
            last += 1

        left = right

    return last

def shift_block(nums, start, end):

    while end<len(nums):
        nums[start], nums[end] = nums[end], nums[start]
        start += 1 
        end += 1 
    

nums = [1,1,1,2,2,3]
remove_dups(nums)
print(nums)

nums = [1,1,1,1,1,2]
remove_dups(nums)
print(nums)

nums = [0,0,1,1,1,1,2,3,3]
remove_dups(nums)
print(nums)