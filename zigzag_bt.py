def zigzag_level_order(root):
    if root==None:
        return []

    Q = [root]
    levels = []
    level_no = 0

    while Q!=[]:
        lev_len = len(Q)
        level = []

        for _ in range(lev_len):
            u = Q.pop(0)
            level.append(u.val)

            if u.left:
                Q.append(u.left)
            if u.right:
                Q.append(u.right)
        
        if level_no%2==0:
            levels.append(level)
        else:
            levels.append(level[::-1])

        level_no += 1

    return levels