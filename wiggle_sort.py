def wiggle_sort(nums):

    n = len(nums)
    if n==1:
        return 
    elif n==2:
        nums.sort()
        return 
    sorted_nums = sorted(nums, reverse=True)

    if n%2==0:
        mid = n//2 
    else:
        mid = n//2+1 
    
    j = 0

    for i in range(1,n,2):
        nums[i] = sorted_nums[j]
        j += 1
        if j==mid:
            break 

    for i in range(0,n,2):
        nums[i] = sorted_nums[j]
        j += 1
        if j==n:
            break

nums = [1,5,1,1,6,4]
wiggle_sort(nums)

nums = [1,3,2,2,3,1]
wiggle_sort(nums)