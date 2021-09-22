def partition_labels(s):

    n = len(s)

    if n==1:
        return [1]

    sdict = dict()
    sizes = []
    sz = 0

    for i in range(n):
        sdict[s[i]] = sdict.get(s[i], 0) + 1

    started = set() # Stores all the characters which have been seen

    for i in range(n):
        sdict[s[i]] -= 1
        sz += 1
        started.add(s[i])
        if sdict[s[i]] == 0: # We've encountered all the characters of this type
            started.remove(s[i])
            if started==set():
                sizes.append(sz)
                sz = 0
    
    if sz!=0:
        sizes.append(sz)
        
    return sizes

s = "ababcbacadefegdehijhklij"
partition_labels(s)