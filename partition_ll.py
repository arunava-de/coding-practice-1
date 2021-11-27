def partition(head, x):
    if head==None:
        return 

    new_head = ListNode()
    curr_new = new_head
    curr = head

    while curr!=None:
        if curr.val<x:
            temp = ListNode(curr.val)
            curr_new.next = temp 
            curr_new = curr_new.next
        curr = curr.next

    curr = head 
    while curr!=None:
        if curr.val>=x:
            temp = ListNode(curr.val)
            curr_new.next = temp 
            curr_new = curr_new.next 
        curr = curr.next

    return new_head.next 

         
            