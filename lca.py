def lowest_common_ancestor(root, p, q):

    if p==root or q==root:
        return root 

    path1 = find_path(root, p)
    path2 = find_path(root, q)

    for i in range(min(len(path1), len(path2))):
        if path1[i]!=path2[i]:
            break 

    return path1[i-1]

def find_path(u, v):

    path = [u]
    S = []
    S.append(u)

    def DFS(x, path, v):

        if x==None: # At a dead end 
            return False 

        path.append(x) 
            
        if DFS(x.left, path) or DFS(x.right, path):
            return True 

        path.pop()

        return False 

    DFS(u, path, v)
    return path 

    