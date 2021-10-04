def reverse_bits(n):

    res = 0
    n = bin(n)[2:]

    for i in range(31, -1, -1):
        if n[i]=='0':
            continue 
        else:
            res += 2**i 

    return res 

n = 12223
reverse_bits(n)

    