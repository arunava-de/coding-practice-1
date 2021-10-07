def inorder(root):

    res = [] 
    S = [root]

    while S:
        while u!=None:
            S.append(u)
            u = u.left

        u = S.pop()
        res.append(u.val)
        u = u.right

    return res 



        
