from math import log2

def get_sum(a, b):

    a = 2**a 
    b = 2**b 

    # Edge case when a+b = 0
    if a*b==1:
        return 0

    return int(log2(a*b))

get_sum(12,5)
get_sum(-5,5)