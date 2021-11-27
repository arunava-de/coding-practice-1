def partition(head, x):

    if head==None or head.next==None:
        return head 

    lesser = ListNode(0)
    greater = ListNode(0)

    prev_l = lesser
    prev_g = greater

    curr = head 

    while curr!=None:
        nxt = curr.next 

        if curr.val<x:
            prev_l.next = curr 
            curr = nxt
            prev_l = prev_l.next 
        else:
            prev_g.next = curr
            curr = nxt 
            prev_g = prev_g.next 

    prev_l.next = greater.next 
    prev_g.next = curr 
    return lesser.next 
