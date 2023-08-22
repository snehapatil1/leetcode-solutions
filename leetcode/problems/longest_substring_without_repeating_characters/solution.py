class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = ""
        max_len = 0

        for idx in range(len(s)):
            if s[idx] in sub_string:
                s_index = sub_string.index(s[idx])
                sub_string = sub_string[s_index + 1:]
            sub_string += s[idx]
            max_len = max(max_len, len(sub_string))
        
        return max_len