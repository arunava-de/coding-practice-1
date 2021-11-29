def gray_code(n):
    out = [0]
    for i in range(1,n+1):
        out += [2**(i-1) + c for c in out[::-1]]

    return out