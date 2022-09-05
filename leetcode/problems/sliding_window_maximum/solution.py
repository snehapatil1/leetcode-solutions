from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        opt = []
        q = collections.deque()
        for i in range(len(nums)):
            n = nums[i]
            
            if q and q[0]<=i-k:
                q.popleft()

            while q and nums[q[-1]]<=n: 
                q.pop()

            q.append(i)

            if 1+i>=k: 
                opt.append(nums[q[0]])
        return opt
                    
            