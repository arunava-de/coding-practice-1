class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if root==None:
        return 0 

    return max(max_depth(root.left), max_depth(root.right)) + 1