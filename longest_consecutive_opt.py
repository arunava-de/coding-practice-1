def longest(nums):

    res = 0
    num_set = set(nums)

    for num in num_set:
        if num-1 not in num_set:
            curr_num = num 
            curr = 1

            while curr_num + 1 in num_set:
                curr_num += 1
                curr += 1

            res = max(res, curr)

    return res 
