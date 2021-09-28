# Delete a node of a LL, you're given the node directly and not the head

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def delete_node(node):

    # nxt = node.next
    prv = None
    curr = node

    while curr.next!=None:
        prv = curr
        nxt = curr.next
        # next_val = nxt.val
        curr.val = nxt.val 
        curr = nxt 

    prv.next = None 



    