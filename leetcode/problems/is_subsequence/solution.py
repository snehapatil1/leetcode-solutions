class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        sPtr, tPtr = 0, 0

        while True:
            if sPtr == len(s):
                return True
            if tPtr == len(t):
                return False
            if s[sPtr] == t[tPtr]:
                sPtr += 1
            tPtr += 1
        return False