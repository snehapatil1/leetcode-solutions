class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        new_s = []
        new_string = ""
        for word in words:
            new_word = ""
            word_arr = list(word)
            word_arr.reverse()
            new_word = new_word.join(word_arr)
            new_s.append(new_word)
            new_s.append(" ")
        
        return new_string.join(new_s).strip()