class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for row in range(len(mat)):
            ones = mat[row].count(1)
            heapq.heappush(heap, (ones, row))
        
        output = []
        while k:
            _, row = heapq.heappop(heap)
            output.append(row)
            k -= 1
        return output