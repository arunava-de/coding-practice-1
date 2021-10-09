def longest(nums):

    n = len(nums)
    if n==1:
        return 1

    opt = [0]*(n+1)
    opt[0] = 1

    for i in range(1, n+1):
        maxlen = -float('inf')
        for j in range(1,i):
            if nums[j-1]<nums[i-1]:
                maxlen = max(maxlen, opt[j])
        opt[i] = max(maxlen,0) + 1 

    return max(opt)

nums = [10,9,2,5,3,7,101,18]
longest(nums)

nums = [0,1,0,3,2,3]
longest(nums)

nums = [7,7,7,7,7,7,7]
longest(nums)

nums = [1,3,6,7,9,4,10,5,6]
longest(nums)