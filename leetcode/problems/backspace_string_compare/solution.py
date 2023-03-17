class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        astack = []
        for lt in list(s):
            if lt.isalpha():
                astack.append(lt)
            if lt == '#' and astack:
                astack.pop()
        s = ''.join(astack)

        bstack = []
        for lt in list(t):
            if lt.isalpha():
                bstack.append(lt)
            if lt == '#' and bstack:
                bstack.pop()
        t = ''.join(bstack)

        return s == t
