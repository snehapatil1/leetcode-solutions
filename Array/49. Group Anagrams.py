"""
    Question:
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
        typically using all the original letters exactly once.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}

        for word in strs:
            sorted_string = ''.join(sorted(word))
            if sorted_string not in anagrams_map.keys():
                anagrams_map[sorted_string] = []
            anagrams_map[sorted_string].append(word)
        
        output = []
        for key in anagrams_map:
            output.append(anagrams_map[key])
        
        return output
