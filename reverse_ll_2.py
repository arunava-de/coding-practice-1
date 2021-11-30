class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create(self, arr):
        n = len(arr)
        i = 0
        head = None
        curr = None

        while i<n:
            if head==None:
                head = ListNode(arr[i])
                curr = head 
            else:
                curr.next = ListNode(arr[i])
                curr = curr.next
            i += 1
        
        return head 
    
    def print_list(self):
        while self!=None:
            print(self.val, end=" ")
            self = self.next

        print()

head = ListNode().create([1,2,3,4,5])
left = 1
right = 4

def reverse_between(head, left, right):
    if head==None or head.next==None:
        return head 

    if left==right:
        return head 

    dummy_head = ListNode(0)
    dummy_head.next = head

    k = 1
    curr = head  
    start_prev = dummy_head
    while k<left:
        start_prev = curr
        curr = curr.next 
        k += 1 
    start = curr 

    curr = start 
    nxt = start 
    prev = start_prev
    k = right - left

    while k>=0:
        nxt = curr.next 
        curr.next = prev 
        prev = curr 
        curr = nxt 
        k -= 1
        
    start_prev.next = prev
    # prev.next = nxt 
    start.next = nxt

    return dummy_head.next