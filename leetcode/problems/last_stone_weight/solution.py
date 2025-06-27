class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-weight for weight in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            y = - heapq.heappop(heap)
            x = - heapq.heappop(heap)

            if x < y:
                y -= x
                heapq.heappush(heap, -y)
        
        return -heap[0] if len(heap) > 0 else 0