class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.scores = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.scores) < self.k or self.scores[0] < val:
            heapq.heappush(self.scores, val)
            if len(self.scores) > self.k:
                heapq.heappop(self.scores)
        return self.scores[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)