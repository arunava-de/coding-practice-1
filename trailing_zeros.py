def trailing_zeros(n):

    twos = 0
    fives = 0

    for i in range(1,n+1):
        curr = i
        while curr%2==0:
            twos += 1
            curr = curr//2 
        curr = i
        while curr%5==0:
            fives += 1
            curr = curr//5

    return min(twos, fives)

trailing_zeros(200)
