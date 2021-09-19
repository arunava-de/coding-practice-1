class MaxHeap:
	def __init__(self):
		self.heap = []
		self.N = 0

	def is_empty(self):
		return self.heap==[]

	def getmax(self):
		return self.heap[0]

	def insert(self, v):
		self.heap.append(v)
		self.N += 1

		curr = self.N - 1

		while curr>0:
			parent = (curr-1)//2
			if self.heap[parent]<self.heap[curr]:
				self.heap[parent], self.heap[curr] = self.heap[curr], self.heap[parent]
				curr = parent
			else:
				break

	def deletemax(self):
		last = self.heap[-1]
		val = self.heap[0]
		self.heap[0] = last 
		self.heap.pop()
		self.N -= 1

		curr = 0

		while curr<self.N:
			cand = 2*curr+1
			if 2*curr+1>=self.N:
				break 
			if cand+1<self.N:
				if self.heap[cand+1]>self.heap[cand]:
					cand += 1 

			if self.heap[cand]>self.heap[curr]:
				self.heap[cand], self.heap[curr] = self.heap[curr], self.heap[cand]
				curr = cand 
			else:
				break
		
		return val 

class MinHeap:

	def __init__(self):
		self.heap = []
		self.N = 0

	def isempty(self):
		return self.heap == []
	
	def insert(self,v):
		self.heap.append(v)
		self.N = self.N+1
		curr = self.N - 1
		while (curr > 0): # I am not the root
			parent = (curr - 1)//2
			if (self.heap[parent] > self.heap[curr]):
				self.heap[parent],self.heap[curr] = self.heap[curr],self.heap[parent]
				curr = parent
			else:
				break
	
	def deletemin(self):
		val = self.heap[0]
		last = self.heap.pop()
		self.N = self.N - 1
		if (self.heap != []):
			self.heap[0] = last
			curr = 0
			while (curr < self.N):
				if (2*curr + 1 >= self.N):
					break
				candidate = 2*curr+1
				if (candidate + 1 < self.N):
					if self.heap[candidate+1] < self.heap[candidate]:
						candidate = candidate+1
				if (self.heap[curr] > self.heap[candidate]):
					self.heap[curr],self.heap[candidate] = self.heap[candidate],self.heap[curr]
					curr = candidate
				else:
					break
	
		return (val)
	
	def getmin(self):
		return self.heap[0]

class MedianFinder:

	def __init__(self):
		self.lo = MaxHeap()
		self.hi = MinHeap()

	def addNum(self, num: int):

		self.lo.insert(num)
		out = self.lo.deletemax()
		self.hi.insert(out)

		if self.hi.N>self.lo.N:
			out_more = self.hi.deletemin()
			self.lo.insert(out_more)

	def findMedian(self):
		
		if self.lo.N==self.hi.N:
			left = self.lo.getmax()
			right = self.hi.getmin()
			return (left+right)/2
		else:
			return self.lo.get(max)


med = MedianFinder()
med.addNum(1)
med.addNum(2)
med.findMedian