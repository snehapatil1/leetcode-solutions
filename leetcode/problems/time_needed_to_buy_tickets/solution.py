from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        
        self.time_taken = 0
        
        self.rec(queue, k)
        
        return self.time_taken
    
    def rec(self, queue, k):
        for idx, ele in enumerate(queue):
            if ele:
                queue[idx] -= 1
                if idx == k and not queue[idx]:
                    self.time_taken += 1
                    return self.time_taken
                else:
                    self.time_taken += 1
        self.rec(queue, k)