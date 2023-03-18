class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_arr = s.split()
        return len(s_arr[-1])
