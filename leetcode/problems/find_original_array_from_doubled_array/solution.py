import heapq
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        output = []
        heap = []
        changed.sort()

        for num in changed:
            if heap and num == heap[0]*2:
                output.append(heapq.heappop(heap))
            else:
                heapq.heappush(heap, num)
        
        return output if not heap else []