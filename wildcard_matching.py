def is_match(s, p):
    ns = len(s)
    np = len(p)

    opt = [[False]*(np+1) for _ in range(ns+1)]
    opt[0][0] = True 

    # Take care of preceding *'s 
    for j in range(1, np+1):
        if p[j-1]!='*':
            break 
        opt[0][j] = True 

    for i in range(1, ns+1):
        for j in range(1, np+1):
            if p[j-1]==s[i-1] or p[j-1]=='?':
                opt[i][j] = opt[i-1][j-1]
            elif p[j-1]=='*':
                opt[i][j] = opt[i-1][j-1] or opt[i-1][j] or opt[i][j-1]
    
    return opt[-1][-1]

    
