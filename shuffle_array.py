import random 

class Solution:

    def __init__(self, nums):
        self.arr = nums 
        # self.shuffled = [0]*len(nums)
        self.n = len(nums)

    def reset(self):
        return self.arr

    def shuffle(self):
        shuffled = [0]*self.n
        i = 0
        seen = set()

        while len(seen)<self.n:
            idx = random.randint(0, self.n-1)
            if idx in seen:
                continue 
            shuffled[i] = self.arr[idx]
            i += 1
            seen.add(idx)

        return shuffled