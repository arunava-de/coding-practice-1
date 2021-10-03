# Divide and conquer approach

def majority(nums):

    n = len(nums)

    def recur(l, r):
        if l==r:
            return nums[l]

        mid = (l+r)//2
        left = recur(l, mid)
        right = recur(mid+1, r)

        if left==right: # No issues here
            return left

        # Now we need to check out of left and right, which occurs more times 

        left_count = sum(1 for i in range(l, r+1) if nums[i]==left)
        right_count = sum(1 for i in range(l, r+1) if nums[i]==right)

        return left if left_count>right_count else right 

    return recur(0,n-1)

    