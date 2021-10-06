class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def ll_to_list(nums):

    head = ListNode() 
    curr = head
    for a in nums:
        curr.next = ListNode(a)
        curr = curr.next
    
    return head.next


def is_palindrome(head):

    curr = head 

    def recur(head):
        nonlocal curr
        if head!=None:
            if not recur(head.next):
                return False 
            if curr.val!=head.val:
                return False 
            curr = curr.next
        return True 
    
    return recur(head)

head = ll_to_list([1,2,3,4])
is_palindrome(head)
