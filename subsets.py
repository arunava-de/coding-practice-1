def subsets(nums):
    if nums==[]:
        return [[]]

    n = len(nums)

    output = []

    def recur(first, curr, k):
        if len(curr)==k:
            output.append(curr[:])

        for i in range(first, n):
            curr.append(nums[i])
            recur(i+1, curr, k)
            curr.pop()

    for k in range(n+1):
        recur(0, [], k)

    return output
        


    


        