from ll_to_bst import TreeNode

def to_bst(head):

    copy = head 
    c = 0

    while copy!=None:
        copy = copy.next 
        c += 1

    def recur(s, e):
        nonlocal head 
        mid = (s+e)//2

        left = recur(s, mid-1)

        node = TreeNode(head.val)
        node.left = left
        head = head.next

        right = recur(mid+1, e)
        node.right = right 

        return node
    
    return recur(0, c-1)
