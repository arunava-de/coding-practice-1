def reverse_list(head):
    if not head:
        return None 

    prev = None 
    curr = head 
    next = head 

    while next!=None:
        next = curr.next
        curr.next = prev 
        prev = curr 
        curr = next 

    return prev