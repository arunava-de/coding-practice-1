def merge(nums1, m, nums2, n):

    if m==0 and n==0:
        return [] 

    k = m+n-1
    i = m-1
    j = n-1 

    while k>=0:
        if j<0:
            break 
        if i>=0 and nums2[j]<nums1[i]:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1 
        else:
            nums1[k] = nums2[j]
            j -= 1
