class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        curLen = 0

        for idx, ch in enumerate(s):
            if ch.isdigit():
                curLen *= int(ch)
            else:
                curLen += 1
        
        for idx in range(len(s) - 1, -1, -1):
            ch = s[idx]
            if ch.isdigit():
                curLen /= int(ch)
                k %= curLen
            else:
                if k ==0 or k == curLen:
                    return ch
                else:
                    curLen -= 1