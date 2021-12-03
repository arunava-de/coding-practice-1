from all_bst import get_trees


def num_trees(n):
    if n==0:
        return 0 

    out = [0]*(n+1)
    get_tree_nums(out, 1, n)
    return out[n]

def get_tree_nums(out, start, end):

    if start>end:
        return 1

    if out[end-start+1]!=0:
        return out[end-start+1]

    out[end-start+1] = 0

    for root_val in range(start, end+1):

        num_left = get_tree_nums(out, start, root_val-1)
        num_right = get_tree_nums(out, root_val+1, end)

        out[end-start+1] += num_left*num_right

    return out[end-start+1]

num_trees(3)
num_trees(1)
num_trees(19)

# get_tree_nums(2,6)

