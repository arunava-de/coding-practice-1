def longest(nums):

    n = len(nums)
    
    nums.sort()

    curr = 1
    res = 1

    for i in range(1,n):
        if nums[i]==nums[i-1]+1:
            curr += 1
        elif nums[i]==nums[i-1]:
            continue
        else:
            res = max(curr, res)
            curr = 1
    res = max(res, curr)

    return res

nums = [100,4,200,1,3,2]
longest(nums)

nums = [0,3,7,2,5,8,4,6,0,1]
longest(nums)

nums = [12,13,17,15,14,13,2,6,5]
longest(nums)