def max_window(nums, k):
    n = len(nums)

    if n==k:
        return [max(nums)]

    res = []
    start = 0
    end = k-1

    while end<n:
        maxx = -10**9
        for i in range(start, end+1):
            if nums[i]>maxx:
                maxx = nums[i]

        res.append(maxx)
        end += 1 
        start += 1

    return res 

nums = [1]
k = 1 
max_window(nums, k)

nums = [1, -1]
k = 1 
max_window(nums, k)

nums = [9, 11]
k = 2 
max_window(nums, k)

nums = [4, -2]
k = 2
max_window(nums, k)
