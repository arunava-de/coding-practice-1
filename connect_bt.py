def connect(root):
    if root==None:
        return 

    Q = [root]

    while Q:
        level = []
        level_len = len(Q)
        
        for _ in range(level_len):
            u = Q.pop(0)
            level.append(u)
            
            if u.left:
                Q.append(u.left)
            if u.right:
                Q.append(u.right)
                
        for i in range(len(level)-1):
            level[i].next = level[i+1]
            
        level[-1].next = None
        
    return root