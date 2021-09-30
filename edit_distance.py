def min_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    opt = [[0]*(n+1) for _ in range(m+1)] # opt[i][j] is min number of operations to convert word1[:i] to word2[:j]

    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                opt[i][j]=j
            elif j==0:
                opt[i][j] = i
            elif word1[i-1]==word2[j-1]:
                opt[i][j] = opt[i-1][j-1]
            else:
                opt[i][j] = 1 + min(min(opt[i-1][j], opt[i][j-1]), opt[i-1][j-1])
    
    return opt[m][n]

word1 = "horse"
word2 = "ros"
min_distance(word1, word2)
    

