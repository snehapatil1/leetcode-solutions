class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        sub = ''
        sList = list(s)

        for i in sList:
            if i not in sub:
                sub += i
                maxLen = max(maxLen, len(sub))
            else:
                i_index = sub.index(i)
                sub = sub[i_index+1:] + i
        
        return maxLen