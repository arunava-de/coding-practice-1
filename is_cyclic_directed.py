def is_cyclic(G, u, stack, visited):
    stack.append(u)
    visited[u] = 0 # This means u has been added to stack. Hence if we come across a vertex during dfs which has already been
                    #added to the stack, it's a cycle
    
    for v in G[u]:
        if visited[v]==-1: # v hasn't been visited before
            if is_cyclic(G, v, stack, visited):
                return True 
        elif visited[v]==0: # v has been visited before and is in stack, hence cycle
            return True 
    
    stack.pop() # We're done exploring all paths from u
    visited[u] = 1 # u popped from stack 

    