def decodings(s):
    inv_encode_dict = dict()

    for i in range(65,91):
        inv_encode_dict[str(i-64)] = chr(i)
    n = len(s)
    opt = [0]*(n+1)

    opt[0] = 1
    opt[1] = 1 if s[0] in inv_encode_dict else 0

    for i in range(2,n+1):
        one = s[i-1:i]
        two = s[i-2:i]

        if one in inv_encode_dict:
            opt[i] += opt[i-1]
        if two in inv_encode_dict:
            opt[i] += opt[i-2]

    return opt[n]

s = "226"
decodings(s)

s = "12"
decodings(s)

s = "0"
decodings(s)

s = "06"
decodings(s)

s = "11106"
decodings(s)