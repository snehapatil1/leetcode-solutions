class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        
        left = 0
        longest = 0
        frequency = defaultdict(int)

        for right in range(len(s)):
            frequency[s[right]] = frequency.get(s[right], 0) + 1
            window = right - left + 1
            max_frequency = max(frequency.values())
            if not window - max_frequency <= k:
                frequency[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)

        return longest