class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        maxLen = 0
        count = {}

        for right in range(n):
            count[s[right]] = count.get(s[right], 0) + 1
            maxLen = max(maxLen, count[s[right]])
            if right - left + 1 - maxLen > k:
                count[s[left]] -= 1
                left += 1
        return right - left + 1