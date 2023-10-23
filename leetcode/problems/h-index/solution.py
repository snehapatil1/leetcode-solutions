class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        if n == 1 and citations[0] == 0:
            return 0
        if n == 1 and citations[0] != 0:
            return 1
        
        h = 1 if citations[0] != 0 else 0
        p1, p2 = 0, 1
        minSoFar = citations[0]

        while p1 <= p2 < n:
            required = p2 - p1 + 1
            if minSoFar >= required:
                p2 += 1
                h = max(h, required)
            else:
                if p2 == p1: p2 += 1
                p1 += 1
            if p1 < n:
                minSoFar = citations[p1]
        
        return h