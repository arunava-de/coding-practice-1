def kthSmallest(root, k):
    S = []
    
    while True:
        while root!=None:
            S.append(root)
            root = root.left
            
        root = S.pop()
        k -= 1
        if k==0:
            return root.val
        root = root.right