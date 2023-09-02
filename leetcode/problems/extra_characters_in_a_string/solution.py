class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n, words = len(s), set(dictionary)

        @cache
        def dp(start):
            if start == n:
                return 0
            ans = dp(start + 1) + 1
            for end in range(start, n):
                cur = s[start:end + 1]
                if cur in words:
                    ans = min(ans, dp(end + 1))
            return ans
        
        return dp(0)