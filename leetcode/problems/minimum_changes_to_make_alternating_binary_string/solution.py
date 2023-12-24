class Solution:
    def minOperations(self, s: str) -> int:
        zeros, ones = 0, 0

        for idx in range(len(s)):
            if (idx % 2 == 0 and s[idx] != '0') or (idx % 2 and s[idx] != '1'):
                zeros += 1
            if (idx % 2 == 0 and s[idx] != '1') or (idx % 2 and s[idx] != '0'):
                ones += 1
        
        return min(zeros, ones)