"""
    Question:
        An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, 
        and then randomly shuffling the resulting array.
        Given an array changed, return original if changed is a doubled array. 
        If changed is not a doubled array, return an empty array. 
        The elements in original may be returned in any order.
"""

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
