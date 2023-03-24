class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        start = 0
        end = len(s)
        count = 0

        while start <= end - 2:
            substring = set(s[start : start + 3])
            if len(substring) == 3:
                count += 1
            start += 1

        return count
