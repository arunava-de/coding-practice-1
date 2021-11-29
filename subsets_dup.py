def subsets_with_dup(nums):
    if nums==[]:
        return [[]]

    n = len(nums)
    nums.sort()
    output = [] 

    def recur(first, curr, k):
        if len(curr)==k:
            output.append(curr[:])

        for i in range(first, n-1):
            if nums[i]==nums[i+1]:
                continue 
            curr.append(nums[i])
            recur(i+1, curr)
            curr.pop()
        
        curr.append(nums[-1])
            recur(n, curr)
            curr.pop()
