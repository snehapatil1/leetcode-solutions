class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        str1_len = len(str1)
        str2_len = len(str2)
        
        if str1_len < str2_len:
            return False
        
        char_dict = {
            'a': 'b',
            'b': 'c',
            'c': 'd',
            'd': 'e',
            'e': 'f',
            'f': 'g',
            'g': 'h',
            'h': 'i',
            'i': 'j',
            'j': 'k',
            'k': 'l',
            'l': 'm',
            'm': 'n',
            'n': 'o',
            'o': 'p',
            'p': 'q',
            'q': 'r',
            'r': 's',
            's': 't',
            't': 'u',
            'u': 'v',
            'v': 'w',
            'w': 'x',
            'x': 'y',
            'y': 'z',
            'z': 'a'
        }
        
        str1_ptr, str2_ptr = 0, 0
        
        while str2_ptr < str2_len:
            if str1_ptr == str1_len:
                return False
            
            s2 = str2[str2_ptr]
            s1 = str1[str1_ptr]
            
            if s2 == s1 or char_dict[s1] == s2:
                str2_ptr += 1
            
            str1_ptr += 1
        
        return True
        
        
        