# Merge two arrays inplace, nums1 has extra space to accommodate nums2

def merge(nums1, m, nums2, n):

    if m==0 and n==0:
        return [] 

    k = m # Denotes index in 0s of nums1
    i = 0 # Denotes index in nums1 from 0 to m-1
    j = 0# Denotes index in nums2 from 0 to n-1

    while i<m+n and j<n:
        if nums1[i]<=nums2[j]:
            i += 1

        else: # nums2[j]<nums1[i]
            # nums1[i], nums1[k] = nums1[k], nums1[i]
            # k += 1
            for l in range(k, i, -1):
                nums1[l] = nums1[l-1]

            k += 1
            nums1[i] = nums2[j]
            j += 1
            i += 1
    
    while j<n:
        nums1[k] = nums2[j]
        k += 1
        j += 1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
merge(nums1, m, nums2, n)
        
nums1 = [1]
nums2 = []
m = 1
n = 0
merge(nums1, m, nums2, n)

nums1 = [0] 
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)

nums1 = [1,2,4,5,6,0]
nums2 = [3]
m = 5
n = 1
merge(nums1, m, nums2, n)