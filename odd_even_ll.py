class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def odd_even(head):

    if head==None:
        return 
    odd = head 
    even = head.next
    evenhead = even 

    while even!=None and even.next!=None:
        odd.next = even.next 
        odd = odd.next 
        even.next = odd.next 
        even = even.next 

    odd.next = evenhead 

    return head 




        

