class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        left = 0
        hmap = {}
        for right in range(len(s)):
            if s[right] in hmap:
                left = max(left, hmap[s[right]] + 1)
            hmap[s[right]] = right
            output = max(output, right - left + 1)

        return output