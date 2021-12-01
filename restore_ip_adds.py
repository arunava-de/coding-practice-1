def restore(s):
    n = len(s)
    if n<4:
        return []

    def recur(rem, dots, curr, out): # rem stores remaining part of s
        if dots>4:
            return 
        if dots==4 and not rem:
            out.append(curr[:-1])
            return 

        for i in range(1, len(rem)+1):
            if rem[:i]=='0' or (rem[0]!='0' and 0<int(rem[:i])<256):
                recur(rem[i:], dots+1, curr+rem[:i]+'.', out)

    out = [] 
    recur(s, 0, '', out)

    return out 

s = "25525511135"
restore(s)
