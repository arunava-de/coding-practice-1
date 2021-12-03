def generate(n):
    if n==0:
        return [] 

    return get_trees(1,n)

def get_trees(start, end):

    if start>end:
        return [None]

    all_trees = []

    for root_val in range(start, end+1):
        all_left = get_trees(start, root_val-1)
        all_right = get_trees(root_val+1, end)

        for left in all_left:
            for right in all_right:
                curr = TreeNode(root_val)
                curr.left = left 
                curr.right = right 

                all_trees.append(curr)

    return all_trees