def lowest_common_ancestor(root, p, q):

    ans = None 

    def DFS(node):
        nonlocal ans 
        if node==None:
            return False 
        if node==p or node==q:
            mid = True 

        left = DFS(node.left)
        right = DFS(node.right)

        if left+right+mid>=2: # Both are found, and this is the first node for which this holds 
            ans = node 
        
        return mid or left or right 
    
    DFS(root)
    return ans 
