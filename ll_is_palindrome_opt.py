class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_ll(nums):

    head = ListNode() 
    curr = head
    for a in nums:
        curr.next = ListNode(a)
        curr = curr.next
    
    return head.next

def find_mid(head):
    fast = head 
    slow = head 

    while fast.next!=None and fast.next.next!=None:
        fast = fast.next.next
        slow = slow.next

    return slow

def reverse(head):
    prv = None 
    curr = head 
    nxt = head 

    while nxt!=None:
        nxt = curr.next 
        curr.next = prv 
        prv = curr 
        curr = nxt 

    return prv 

def is_palindrome(head):
    if head.next==None:
        return True 

    mid = find_mid(head)
    first = head
    second = reverse(mid.next)
    result = True
    while result and second!=None:
        if first.val!=second.val:
            return False 
        first = first.next
        second = second.next

    return result

nums = [1,2,3,4,5]
is_palindrome(list_to_ll(nums))

nums = [1,2,3,2,1]
is_palindrome(list_to_ll(nums))




