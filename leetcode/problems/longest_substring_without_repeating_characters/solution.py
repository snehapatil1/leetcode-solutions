class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        left = 0
        visited = {}

        for right in range(len(s)):
            if s[right] in visited:
                left = max(left, visited[s[right]])
            visited[s[right]] = right + 1
            maxlen = max(maxlen, right - left + 1)
        
        return maxlen