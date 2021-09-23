def k_most_frequent(nums, k):

    n = len(nums)
    if n==1:
        return nums

    numsdict = {}

    for i in range(n):
        numsdict[nums[i]] = numsdict.get(nums[i], 0) + 1

    freq_tuples = []

    for num in numsdict:
        freq_tuples.append((num, -numsdict[num]))
    
    # Now we can do quick sort partition on the tuples based on 2nd index

    quickselectK(freq_tuples, 0, len(freq_tuples)-1, k)
    return [f[0] for f in freq_tuples[:k]]


def quickselectK(arr, start, end, k):
    if start<end:
        pi = partition(arr, start, end)
        left = pi-start+1

        if k<left:
            quickselectK(arr, start, pi-1, k)
        elif k>left:
            quickselectK(arr, pi+1, end, k-left)
    else:      
        return 

def partition(arr, l, r):
 
    pivot = arr[l][1]
    idx = l

    while l<r:

        while l<r and arr[l][1]<=pivot:
            l += 1

        while arr[r][1]>pivot:
            r -= 1
        
        if l<r:
            arr[l], arr[r] = arr[r], arr[l]

    arr[r], arr[idx] = arr[idx], arr[r]

    return r

nums = [1,1,1,2,2,3]
k = 2
k_most_frequent(nums, k)

nums = [1,2,3,2,7,5,5,7,4,4,2,4,12,0,9,2]
k = 4
k_most_frequent(nums, k)





