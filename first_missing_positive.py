def first_miss(nums):

    lowest_pos = 10**9
    highest = max(nums)
    
    if highest<1:
        return 1 

    for k in nums:
        if k>0 and k<lowest_pos:
            lowest_pos = k

    if lowest_pos>1:
        return 1 

    for k in range(lowest_pos, highest+1):
        if k not in nums and k>0:
            return k 

    return highest+1

nums = [1,2,0]
first_miss(nums)

nums = [3,4,-1,1]
first_miss(nums)

nums = [7,8,9,11,12]
first_miss(nums)

nums = [1000, -1]
first_miss(nums)
