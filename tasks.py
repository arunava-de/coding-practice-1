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

