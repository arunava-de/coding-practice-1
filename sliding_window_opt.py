def max_window(nums, k):
    n = len(nums)
    res = [] 
    if n==0:
        return res
    if k>n:
        return res 

    window = [] # Stores indices of max window
    for i in range(k):
        while window and nums[i]>=nums[window[-1]]:
            window.pop()
        window.append(i)
    
    res.append(nums[window[0]])

    for i in range(k, n):

        while window and nums[i]>=nums[window[-1]]:
            window.pop()

        # Check if first num in the window is falling in current window or not 

        if window and window[0]<=i-k:
            window.pop(0)

        window.append(i)
        res.append(nums[window[0]])

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