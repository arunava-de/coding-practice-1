#  This time array is sorted

def binary_search(nums, v):

    low = 0
    high = len(nums)-1

    while low<=high:
        mid = (low+high)//2

        if nums[mid]==v:
            return mid 
        elif v>nums[mid]:
            low = mid+1
        else:
            high = mid-1


def twoSum(nums, target):

    n = len(nums)

    if n==2:
        return [1,2] # Since the pair is guaranteed to exist

    numsdict = dict()
    for i in range(n):
        numsdict[nums[i]] = numsdict.get(nums[i], 0) + 1

    for i in range(n):
        curr = nums[i]

        if target-curr in numsdict:
            if curr==target-curr and numsdict[curr]>1:
                return [i+1, i+2]
            elif curr!=target-curr:
                break 

    # Now we do binary search to find target-curr

    j = binary_search(nums, target-curr)

    return [min(i,j)+1, max(i,j)+1]


nums = [2,2,11,15]
target = 4
twoSum(nums, target)