class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap = []
        counter = 0
        
        for i in range(len(dist)):
            heap.append(dist[i] / speed[i])
        heapq.heapify(heap)
        
        while heap:
            if heapq.heappop(heap) <= counter:
                break
            
            counter += 1
        
        return counter