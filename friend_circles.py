class DSet:

    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1]*n

    def find(self, idx):
        if self.parents[idx]==idx:
            return idx 

        self.parents[idx] = self.find(self.parents[idx])

        return self.parents[idx]

    def union(self, idx1, idx2):

        p1 = self.find(idx1)
        p2 = self.find(idx2)

        if p1==p2:
            return 

        if self.rank[p1]<self.rank[p2]:
            self.parents[p2] = p1 
        elif self.rank[p2]<self.rank[p1]:
            self.parents[p1] = p2 
        else:
            self.parents[p1] = p2 
            self.rank[p2] += 1 

def find_friends(isConnected):

    n = len(isConnected)

    if n==1:
        return 1 

    circles = DSet(n)

    for i in range(n):
        for j in range(i+1,n):
            if isConnected[i][j]==1:
                circles.union(i,j)
    
    comps = set() 
    for i in range(n):
        comps.add(circles.find(i))

    return len(comps)

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
find_friends(isConnected)

isConnected = [[1,0,0],[0,1,0],[0,0,1]]
find_friends(isConnected)
