class MinHeap:
    def __init__(self):
        self.heap = []
        self.N = 0 

    def insert(self, v):
        self.heap.append(v)
        self.N += 1 
        curr = self.N - 1 

        while curr>0:
            parent = (curr-1)//2
            if self.heap[parent][0] > self.heap[curr][0]:
                self.heap[parent], self.heap[curr] = self.heap[curr], self.heap[parent]
                curr = parent 
            else:
                break 
    
    def delete_min(self):
        last = self.heap[-1]
        val = self.heap[0]
        self.heap.pop()
        self.N -= 1

        if self.heap==[]:
            return val 

        self.heap[0] = last 

        curr = 0 

        while curr<self.N:
            cand = 2*curr + 1
            if cand>=self.N:
                break 
            if cand+1<self.N:
                if self.heap[cand+1][0]<self.heap[cand][0]:
                    cand = cand + 1

            if self.heap[curr][0]>self.heap[cand][0]:
                self.heap[curr], self.heap[cand] = self.heap[cand], self.heap[curr]
                curr = cand 
            else:
                break 

        return val 


def kth_smallest(matrix, k):
    n = len(matrix)
    if n==1:
        return matrix[0][0]

    heap = MinHeap()

    for r in range(n):
        heap.insert((matrix[r][0], r, 0)) # Create heap of 3-tuples

    rank = 0

    while heap.N>0:
        temp = heap.delete_min()
        rank += 1

        if k==rank:
            return temp[0]
            # print(temp[0])

        if temp[2]+1<n: 
            next = (matrix[temp[1]][temp[2]+1], temp[1], temp[2]+1)
            # print(next)
            # print("Heap:",heap.heap)
            heap.insert(next)

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
kth_smallest(matrix, k)

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 4
kth_smallest(matrix, k)

matrix = [[1,2],[3,3]]
k = 4
kth_smallest(matrix, k)