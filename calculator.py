def calculate(s):
    n = len(s)
    # res = 0 
    S = []
    curr = ""
    op = "+"

    def divide(a, b):
        sign_a = -1 if a<0 else 1
        sign_b = -1 if b<0 else 1
        a = abs(a)
        b = abs(b)
        div = a//b 
        return div if sign_a==sign_b else -div

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
                S.append(divide(prev, int(curr)))
            op = s[i]
            curr = ""
            
    
    res = 0
    while S!=[]:
        res += S.pop()

    return res 
        
s = "3*2+2"
calculate(s)

s = " 3/2 "
calculate(s)

s = " 3+5 / 2 "
calculate(s)

s = "14-3/2"
calculate(s)