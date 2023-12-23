class Solution:
    def maxScore(self, s: str) -> int:
        # maxScore = 0
        
        # for idx in range(1, len(s)):
        #     maxScore = max(maxScore, s[:idx].count('0') + s[idx:].count('1'))
        
        # return maxScore

        ones = s.count('1')
        zeros = 0
        maxScore = 0

        for idx in range(len(s) - 1):
            if s[idx] == '1':
                ones -= 1
            else:
                zeros += 1
            
            maxScore = max(maxScore, zeros + ones)

        return maxScore