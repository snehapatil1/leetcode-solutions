import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = collections.Counter(s)
        output = ""
        heap = []
        
        for ch in counts:
            heapq.heappush(heap, (-counts[ch], ch))
        heapq.heapify(heap)

        while len(heap) >= 2:
            remaining1, ch1 = heapq.heappop(heap)
            remaining1 = -remaining1
            remaining2, ch2 = heapq.heappop(heap)
            remaining2 = -remaining2
            
            if output and output[-1] == ch1: return ""
            output += ch1

            if remaining1 > 1:
                heapq.heappush(heap, (-(remaining1 - 1), ch1))
            
            if output and output[-1] == ch2: return ""
            output += ch2
            
            if remaining2 > 1:
                heapq.heappush(heap, (-(remaining2 - 1), ch2))
        
        if heap:
            remaining, ch = heapq.heappop(heap)
            if -remaining > 1:
                return ""
            output += ch
        
        return output
