def find_single(nums):
    seen = set()
        
    for n in nums:
        if n not in seen:
            seen.add(n)
        else:
            seen.remove(n)

    return tuple(seen)[0]


    
