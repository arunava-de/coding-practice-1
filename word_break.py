def word_break(s, wordDict):
    
    n = len(s)

    opt = [False]*(n+1)

    opt[0] = True 

    for i in range(1, n+1):
        for j in range(i):
            s2 = s[j:i]

            if opt[j]==True and s2 in wordDict:
                opt[i] = True 
                break 
    
    return opt[n]

word_break("leetcode", ["leet","code"])

