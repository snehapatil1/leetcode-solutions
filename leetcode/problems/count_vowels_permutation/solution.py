class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        a = e = i = o = u = 1

        for _ in range(1, n):
            aNext = e
            eNext = (a + i) % MOD
            iNext = (a + e + o + u) % MOD
            oNext = (i + u) % MOD
            uNext = a
        
            a, e, i, o, u = aNext, eNext, iNext, oNext, uNext
        
        return (a + e + i + o + u) % MOD