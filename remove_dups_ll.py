def remove_duplicates(head):

    if head==None:
        return 

    prev = None 
    curr = head 

    while curr!=None:
        if prev==None:
            prev = head
            curr = curr.next
        else:
            if prev.val==curr.val:
                prev.next = curr.next 
                curr = curr.next 
            else:
                prev = prev.next 
                curr = curr.next 

    return head 

