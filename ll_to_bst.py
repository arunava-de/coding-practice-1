class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def to_list(head):

    nums = []
    while head != None:
        nums.append(head.val)
        head = head.next
    
    return nums 

def to_bst(head):

    if head==None:
        return 
        
    nums = to_list(head)

    n = len(nums)
    root = TreeNode()

    def recur(node, s, e):

        if s==e:
            node.val = nums[s]
            return node 
        if s<e:
            mid = (s+e)//2
            node.val = nums[mid]

            node.left = recur(TreeNode(), s, mid-1)
            node.right = recur(TreeNode(), mid+1, e)

            return node 
        return 
    
    recur(root, 0, n-1)
    return root 