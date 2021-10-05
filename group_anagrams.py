def group_anagrams(strs):
    
    counts_table = dict()

    for s in strs:
        counts = [0]*26

        for c in s:
            counts[ord(c)-ord('a')] += 1

        counts = tuple(counts)

        if counts in counts_table:
            counts_table[counts].append(s)
        else:
            counts_table[counts] = [s]

    return counts_table.values()