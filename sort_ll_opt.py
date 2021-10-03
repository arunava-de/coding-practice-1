from ll_to_bst import ListNode


def get_mid(head):

    midprev = None 
    while head!=None and head.next!=None:
        if midprev==None:
            midprev = head 
        else:
            midprev = midprev.next 
        head = head.next.next

    mid = midprev.next 
    midprev.next = None 
    return mid 

def sort_list(head):

    if head==None or head.next==None:
        return head 

    mid = get_mid(head)
    left = sort_list(head)
    right = sort_list(mid)
    return merge(left, right)

def merge(l1, l2):
    head = ListNode()
    tail = head 

    while l1!=None and l2!=None:
        if l1.val<=l2.val:
            tail.next = l1 
            l1 = l1.next
            tail = tail.next
        else:
            tail.next = l2 
            l2 = l2.next
            tail = tail.next 

    if l1==None:
        tail.next = l2 
    else:
        tail.next = l1 

    return head.next 

    