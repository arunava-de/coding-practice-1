def majority(nums):

    numsdict = dict()
    n = len(nums)

    for i in range(n):
        numsdict[nums[i]] = numsdict.get(nums[i], 0) + 1

    return max(numsdict, key=numsdict.get)