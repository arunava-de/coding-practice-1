def calculate(s):
    n = len(s)
    # res = 0 
    S = []
    curr = ""
    op = "+"

    for i in range(n):
        if s[i].isnumeric():
            curr += s[i]
        if (not s[i].isnumeric() and s[i]!=' ') or i==n-1:
            if op=="+":
                S.append(int(curr))
            elif op=="-":
                S.append(-int(curr))
            elif op=="*":
                prev = S.pop()
                S.append(prev*int(curr))
            elif op=="/":
                prev = S.pop()
                S.append(prev//int(curr))
            op = s[i]
            curr = ""
            
    
    res = 0
    while S!=[]:
        res += S.pop()

    return res 
        
s = "3*2+2"