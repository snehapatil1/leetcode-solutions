class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin, cmax= 0, 0

        for i in range(len(s)):
            cmin = cmin + 1 if s[i] == '(' else max(cmin - 1, 0)
            cmax = cmax - 1 if s[i] == ')' else cmax + 1
            if cmax < 0:
                return False
        return cmin == 0

