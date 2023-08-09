class Solution:
    def finalString(self, s: str) -> str:
        new = ''
        i = 0
        while i < len(s):
            if s[i] == 'i':
                new = new[:i][::-1]+new[i + 1:]
            else:
                new += s[i]
            i += 1
        return new