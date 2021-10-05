def product(nums):

    n = len(nums)
    leftprods = [1]*n
    rightprods = [1]*n

    for i in range(1,n):
        leftprods[i] = leftprods[i-1]*nums[i-1]

    for i in range(n-2,-1,-1):
        rightprods[i] = rightprods[i+1]*nums[i+1]

    prods = []

    for i in range(n):
        prods.append(leftprods[i]*rightprods[i])

    return prods

nums = [1,2,3,4]

nums = [-1,1,0,-3,3]