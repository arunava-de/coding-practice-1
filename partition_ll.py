def partition(head, x):
    if head==None:
        return 

    left = head # This signifies the part where all nodes < x ends 
    right = head # This signifies the part where all nodes >= x starts 
    new_head = head 
    curr = head

    while curr!=None: 
        if curr.val<x:
            left.next = curr 
            curr.next = left.next 
            