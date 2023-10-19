class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount = Counter(s)
        sorted(t)
        
        output = 0
        for ch in t:
            if sCount[ch] > 0:
                sCount[ch] -= 1
            else:
                output += 1
        
        return output