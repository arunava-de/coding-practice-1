def find_dup(nums):

    n = len(nums)-1

    return (sum(nums) - n*(n+1)//2)

nums = [1,3,4,2,2]
find_dup(nums)

nums = [3,1,3,4,2]
find_dup(nums)

nums = [1,1,2]
find_dup(nums)

nums = [1,1]
find_dup(nums)

nums = [1,2,2]
find_dup(nums)

nums = list(range(1,2000)) + [148]
find_dup(nums)