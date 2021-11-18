def is_match(s, p):
    ns = len(s)
    np = len(p)

    opt = {}

    def dp(i, j):
        if (i,j) not in opt:
            if j==len(p):
                ans = i==len(s)
            else:
                first = i<len(s) and p[j] in {s[i], '.'}
                if j+1<len(p) and p[j+1]=='*':
                    ans = dp(i,j+2) or first and dp(i+1,j)
                else:
                    ans = first and dp(i+1,j+1)
            opt[(i,j)] = ans 

        return opt[(i,j)]
    
    return dp(0,0)
    

s = "aa"
p = "a"
is_match(s, p)

s = "aa"
p = "a*"
is_match(s, p)

s = "ab"
p = ".*"
is_match(s, p)

s = "aab"
p = "c*a*b"
is_match(s, p)

