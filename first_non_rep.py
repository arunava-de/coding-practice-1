def first_unique(s):

    sdict = dict()

    for c in s:
        sdict[c] = sdict.get(c, 0) + 1

    for i in range(len(s)):
        if sdict[s[i]] == 1:
            return i

    return -1