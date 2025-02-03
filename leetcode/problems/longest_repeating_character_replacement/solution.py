class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        output = 0
        left = 0
        count = defaultdict(int)
        maxFrequency = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxFrequency = max(maxFrequency, count[s[right]])
            while (right - left + 1) - maxFrequency > k:
                count[s[left]] -= 1
                left += 1
            output = max(output, (right - left + 1))

        return output