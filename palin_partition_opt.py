def partition(s):
    n = len(s)

    if n==1:
        return [[s]]

    result = []
    opt = [[False]*n for _ in range(n)]
    opt[0][0] = True 
    
    def recur(start, curr, s, opt):
        nonlocal result
        if start>=len(s):
            result.append(curr[::])

        for end in range(start, len(s)):
            if s[start]==s[end] and (end-start<=2 or opt[start+1][end-1]):
                opt[start][end] = True
                curr.append(s[start:end+1])
                recur(end+1, curr, s, opt)
                curr.pop()
