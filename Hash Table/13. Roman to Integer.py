class Solution:
    def romanToInt(self, s: str) -> int:
        self.hash_table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        roman = list(s)
        number = 0
        
        for idx, letter in enumerate(roman):
            num = self.hash_table[letter]
            
            if idx+1 <= len(roman)-1:
                if (letter == 'I' and roman[idx+1] in ['V', 'X'] \
                   or letter == 'X' and roman[idx+1] in ['L', 'C'] \
                   or letter == 'C' and roman[idx+1] in ['D', 'M']):
                    num = -num
            number += num
