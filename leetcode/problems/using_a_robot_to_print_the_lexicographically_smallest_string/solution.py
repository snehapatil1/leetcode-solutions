class Solution:
    def robotWithString(self, s: str) -> str:
        counts = Counter(s)
        stack = []
        p = ""
        minch = 'a'

        for ch in s:
            stack.append(ch)
            counts[ch] -= 1
            while minch != 'z' and counts[minch] == 0:
                minch = chr(ord(minch) + 1)
            
            while stack and stack[-1] <= minch:
                p += stack.pop()
        
        return p