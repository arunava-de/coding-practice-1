def get_sum(n):
    s = 0

    while n>0:
        s += (n%10)**2
        n = n//10

    return s

def is_happy(n):

    if n==1:
        return True 
    elif n==False:
        return False 

    slow = n 
    fast = n 

    while slow!=1 and fast!=1:
        slow = get_sum(slow)
        fast = get_sum(get_sum(fast))

        if slow==fast and slow!=1:
            return False 

    return True 

is_happy(19)
