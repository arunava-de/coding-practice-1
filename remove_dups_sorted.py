def remove_duplicates(nums):

    n = len(nums)
    if n==0:
        return 0
    elif n==1:
        return 1

    curr = 0 
    next_unique = 1

    while next_unique<n:
        if curr==n-1: # This means all elements are unique
            break 

        if nums[curr]==nums[next_unique]: # We move next_unique forward
            next_unique += 1 
            continue 
        else: # Now we're at the next unique element
            nums[curr+1], nums[next_unique] = nums[next_unique], nums[curr+1]
            curr += 1 
            next_unique += 1
            continue 

    return curr+1

nums = [1,1,2]
remove_duplicates(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
remove_duplicates(nums)

nums = [1,1,1]
remove_duplicates(nums)

nums = [1,2,3,4]
remove_duplicates(nums)