def title_to_number(columnTitle):
    res = 0
    n = len(columnTitle)

    if n==1:
        return ord(columnTitle)-65+1

    for i in range(n):
        res += (ord(columnTitle[i])-65+1)*(26**(n-i-1))

    return res 

title_to_number("FF")
title_to_number("FXSHRXW")