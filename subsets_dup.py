def subsets_with_dup(nums):
    if nums==[]:
        return [[]]

    nums.sort()
    output = [] 
    
    def dfs(curr, nums):

        output.append(curr)

        if len(nums)==0:
            return 

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            dfs(curr+[nums[i]], nums[i+1:])

    dfs([], nums)
    return output 

subsets_with_dup([1,2,2])
