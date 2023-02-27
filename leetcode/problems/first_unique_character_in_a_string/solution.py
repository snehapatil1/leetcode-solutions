import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # collections.Counter creates a dictionary of character wise number of occurrences 
        count = collections.Counter(s)

        for idx, char in enumerate(s):
            # if there exists any character with only 1 occurrence then return it's index
            if count[char] == 1:
                return idx
        
        return -1