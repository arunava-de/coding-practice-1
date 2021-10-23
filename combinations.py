def combine(n, k):

    def recur(curr, res, start):
        nonlocal n 
        nonlocal k
        if len(curr)==k:
            res.append(curr)
            return

        for i in range(start, n+1):
            recur(curr+[i], res, i+1)

    res = [] 
    recur([], res, 1)

    return res 

combine(4,2)