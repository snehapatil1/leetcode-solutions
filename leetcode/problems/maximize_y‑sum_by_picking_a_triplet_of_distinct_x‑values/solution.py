class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        heap = [(-num, idx) for idx, num in enumerate(y)]
        heapq.heapify(heap)
        used = {}
        max_sum = 0

        while len(used.keys()) < 3 and heap:
            ynum, idx = heapq.heappop(heap)
            if idx in used or x[idx] in used.values():
                continue
            used[idx] = x[idx]
            max_sum += -ynum
        
        return max_sum if len(used.keys()) == 3 else -1