class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 0:
            if len(heap) == 1:
                return -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            stone1 = -heapq.heappop(heap)
            if stone1 <= stone2:
                stone2 -= stone1
                heapq.heappush(heap, -stone2)
        
        return 0