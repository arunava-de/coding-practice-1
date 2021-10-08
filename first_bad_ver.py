def firstBadVersion(self, n):

    if n==1:
        return 1 
    
    l = 0
    r = n-1
    
    while l<=r:
        mid = (l+r)//2
        
        if isBadVersion(mid+1):
            r = mid-1
        else:
            l = mid+1
            
    return l+1
    