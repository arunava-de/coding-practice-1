def delete_duplicates(head):

    if head==None:
            return

    curr = head 
    # nxt = curr.next

    while curr!=None:
        nxt = curr.next
        if not nxt:
            break 

        while nxt!=None and curr.val==nxt.val:
            nxt = nxt.next 

        curr.next = nxt 
        curr = curr.next 

    return head