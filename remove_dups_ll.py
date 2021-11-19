def remove_duplicates(head):

    if head==None:
            return 

    prev = None 
    curr = head 
    nxt = head.next 

    while curr!=None and nxt!=None:
        while nxt!=None and curr.val==nxt.val:
            nxt = nxt.next
        if curr.next==nxt: # No duplicates found
            curr = curr.next
            nxt = nxt.next
            if prev==None:
                prev = head
            else:
                prev = prev.next
            prev.next = curr
        else: # Duplicates found 
            if prev!=None:
                prev.next = nxt 
                if nxt==None:
                    break
            curr = nxt 
            nxt = curr.next

    return head 


