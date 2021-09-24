# class MaxHeap:
#     def __init__(self):
#         self.heap = []
#         self.N = 0

#     def is_empty(self):
#         return self.heap==[]

#     def insert(self, t):
#         self.heap.append(t)
#         self.N += 1
#         curr = self.N-1 

#         while curr>0:
#             parent = (curr-1)//2

#             if self.heap[parent][1]<self.heap[curr][1]:
#                 self.heap[curr], self.heap[parent] = self.heap[parent], self.heap[curr]
#                 curr = parent
#             else:
#                 break 
    
#     def deletemax(self):
#         if self.is_empty():
#             return

#         last = self.heap.pop()
#         self.N -= 1
#         val = self.heap[0]
#         self.heap[0] = last
#         curr = 0 

#         while curr<self.N:
#             cand = 2*curr + 1
#             if cand>=self.N:
#                 break 

#             if cand+1<self.N:
#                 if self.heap[cand+1][1]>self.heap[cand][1]:
#                     cand += 1

#             if self.heap[curr][1]<self.heap[cand][1]:
#                 self.heap[curr], self.heap[cand] = self.heap[cand], self.heap[curr]
#                 curr = cand 
#             else:
#                 break 
        
#         return val 

class FreqStack:

    def __init__(self):
        self.freq = dict()
        self.group = dict()
        self.maxfreq = 0

    def push(self, v):
        self.freq[v] = self.freq.get(v, 0) + 1
        
        if self.freq[v] in self.group:
            self.group[self.freq[v]].append(v)
        else:
            self.group[self.freq[v]] = [v]

        if self.freq[v]>self.maxfreq:
            self.maxfreq = self.freq[v]

    def pop(self):
        out = self.group[self.maxfreq].pop()
        self.freq[out] -= 1
        if self.group[self.maxfreq]==[]:
            self.maxfreq -= 1
        
        return out


        
