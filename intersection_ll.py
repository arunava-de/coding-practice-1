def get_intersection(headA, headB):
    currA = headA
    currB = headB 

    nA = 0
    nB = 0

    while currA!=None:
        currA = currA.next 
        nA += 1

    while currB!=None:
        currB = currB.next 
        nB += 1

    diff = max(nA, nB) - min(nA, nB)
    currA = headA
    currB = headB
    if nA<nB:
        while diff>0:
            currB = currB.next 
            diff -= 1 
    elif nB<nA:
        while diff>0:
            currA = currA.next
            diff -= 1
            
    
    while currA!=None and currB!=None and currA!=currB:
        currA = currA.next 
        currB = currB.next
            
    if currA==currB:
        return currA

    return None
