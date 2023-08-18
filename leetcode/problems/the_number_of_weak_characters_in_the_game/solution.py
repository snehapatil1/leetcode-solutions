class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        weak = 0
        queue = []

        for character in range(len(properties)):
            while queue and queue[0][0] < properties[character][1] and queue[0][1] < properties[character][0]:
                weak += 1
                heapq.heappop(queue)
            heapq.heappush(queue, (properties[character][1], properties[character][0]))
        
        return weak