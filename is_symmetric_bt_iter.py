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
    Q = []
    Q.append(root)
    Q.append(root)

    while Q:
        t1 = Q.pop(0)
        t2 = Q.pop(0)

        if t1==None and t2==None:
            continue 
        elif t1==None or t2==None:
            return False
        elif t1.val!=t2.val:
            return False 

        Q.append(t1.left)
        Q.append(t2.right)
        Q.append(t1.right)
        Q.append(t2.left)
    
    return True

        
