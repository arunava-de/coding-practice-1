def level_order(root):

    if root==None:
        return []

    levels = []
    Q = [root]

    while Q:
        levlen = len(Q)
        lv = []

        for _ in range(levlen):
            u = Q.pop()
            lv.append(u.val)

            if u.left:  
                Q.append(u.left)
            if u.right:
                Q.append(u.right)
        
        levels.append(lv)


