class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        pairs = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}
        num = 0
        n = len(s)

        for idx in range(n):
            if s[idx] in pairs.keys():
                if idx < n - 1 and s[idx + 1] in pairs[s[idx]]:
                    num -= hmap[s[idx]]
                else:
                    num += hmap[s[idx]]
            else:
                num += hmap[s[idx]]

        return num