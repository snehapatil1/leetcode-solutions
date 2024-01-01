class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        idx = 0
        count = 0

        while idx < len(s) and count < len(g):
            if s[idx] >= g[count]:
                count += 1
            idx += 1
        
        return count