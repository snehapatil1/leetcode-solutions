class Solution:
    def countHomogenous(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        
        count = 0
        curr = 0
        MOD = 10 ** 9 + 7

        for i in range(n):
            if i == 0 or s[i - 1] == s[i]:
                curr += 1
            else:
                curr = 1
            count = (count + curr) % MOD
        
        return count