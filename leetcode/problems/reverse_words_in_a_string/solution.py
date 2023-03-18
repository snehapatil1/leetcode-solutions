class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        s_list = s.split()
        s_list = s_list[::-1]
        return " ".join(s_list)