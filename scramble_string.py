def is_scramble(s1, s2):
    
    if len(s1)==1:
        return s1==s2 

    if sorted(s1)!=sorted(s2):
        return False 

    n = len(s1)

    for k in range(1, n):
        if is_scramble(s1[:k],s2[:k]) and is_scramble(s1[k:],s2[k:]): # No substitution done
            return True 
        if is_scramble(s1[:k],s2[n-k:]) and is_scramble(s1[k:],s2[:n-k]): # Substitution done
            return True 
    return False 


        


