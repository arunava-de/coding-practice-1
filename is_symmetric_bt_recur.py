class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_mirror(t1, t2):
    if t1==None and t2==None:
        return True 
    elif t1==None or t2==None:
        return False 

    return (t1.val==t2.val) and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

def is_symmetric(root):
    return is_mirror(root, root)
    
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(2)
root.right.left = TreeNode(2)

is_symmetric(root)