class MedianFinder:

    def __init__(self):
        self.l = []
        self.is_sorted = True
        self.size = 0

    def addNum(self, num: int):
        self.l.append(num)
        self.size += 1
        if self.size>1 and self.l[-1]<self.l[-2]:
            self.is_sorted = False 

    def findMedian(self):
        if not self.is_sorted:
            self.l.sort()

        if self.size%2!=0:
            return self.l[self.size//2]
        else:
            return (self.l[self.size//2 - 1] + self.l[self.size//2])/2

