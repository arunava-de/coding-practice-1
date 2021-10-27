def kth_smallest(root, k):

    def inorder(root):

        if root==None:
            return []

        return inorder(root.left) + [root.val] + inorder(root.right)
    
    inord = inorder(root)
    return inord[k-1]