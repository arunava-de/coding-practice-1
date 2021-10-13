def rob(nums):
    n = len(nums)
    if n==1:
        return nums[0]
    elif n==2:
        return max(nums)
    
    opt = [0]*(n+1)
    opt[1] = nums[0]
    
    for i in range(3, n+1):
        opt[i] = max(opt[i-1], opt[i-2]+nums[i-1])
        
    return opt[n]