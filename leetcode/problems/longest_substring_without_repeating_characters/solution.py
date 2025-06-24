class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = defaultdict(int)
        longest = 0
        p1 = 0

        for p2 in range(len(s)):
            if s[p2] in hmap:
                p1 = max(p1, hmap[s[p2]] + 1)
            hmap[s[p2]] = p2
            longest = max(longest, p2 - p1 + 1)
        
        return longest