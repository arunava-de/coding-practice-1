def is_cyclic(head):

    if head==None:
        return False
    slow = head 
    fast = head 

    while slow and fast and fast.next:
        slow = slow.next 
        fast = fast.next.next

        if slow==fast:
            return True 

    return False 