"""
    Question:
        You are given a string text of words that are placed among some number of spaces. 
        Each word consists of one or more lowercase English letters and are separated by at least one space. 
        It's guaranteed that text contains at least one word.
        Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. 
        If you cannot redistribute all the spaces equally, place the extra spaces at the end, 
        meaning the returned string should be the same length as text.    
        Return the string after rearranging the spaces.
"""

class Solution:
    def reorderSpaces(self, text: str) -> str:
        original_length = len(text)
        words = text.split()
        spaces = text.count(" ")
        text.strip()

        if len(words) == 1:
            return words[0] + " "*spaces

        ideal_spaces = spaces // (len(words) - 1)
        remaining_spaces = spaces - (len(words) - 1) * ideal_spaces

        return (" "*ideal_spaces).join(words) + " "*remaining_spaces
