def remove_duplicates(head):

    if head==None:
            return 

    sent = ListNode(0, head)
    prev = sent 

    while head:
        if head.next and head.val==head.next.val:
            while head.next and head.val==head.next.val:
                head = head.next 
            prev.next = head.next 
        else:
            prev = prev.next 

        head = head.next 

    return sent.next 


