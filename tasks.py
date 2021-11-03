def least_interval(tasks, n):
    count = [0]*26
    maxx = 0
    taskmax = 0

    for t in tasks:
        count[ord(t)-65] += 1
        c = count[ord(t)-65]

        if c==maxx:
            taskmax += 1
        elif c>maxx:
            maxx = c
            taskmax = 1 

    return max(len(tasks), (maxx-1)*(n+1) + taskmax)

# (maxx-1)*n are the number of gaps between most frequent elements
# maxx is the frequency count of the most frequent element
# taskmax is the number of most frequent elements
# taskmax - 1 is the number of 'overshooting' elements to be added to the end
# (maxx-1)*n + maxx + taskmax - 1 