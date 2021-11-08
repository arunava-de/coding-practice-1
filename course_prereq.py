
def is_cyclic(u, visited, stack, G):

    stack.append(u)
    visited[u] = 0

    for v in G[u]:
        if visited[v]==-1:
            if is_cyclic(v, visited, stack, G):
                return True 
        elif visited[v]==0:
            return True 

    stack.pop()
    visited[u] = 1

    return False

def canFinish(numCourses, prerequisites):

    if prerequisites==[]:
        return list(range(numCourses))[::-1]

    G = dict()

    for i in range(numCourses):
        G[i] = set()

    for p in prerequisites:
        G[p[1]].add(p[0])

    #If cyclic, then courses can't be completed

    visited = {}
    for u in range(numCourses):
        visited[u] = -1

    stack = []

    for u in G.keys():

        if is_cyclic(u, visited, stack, G):
            return False

    return True 
    
