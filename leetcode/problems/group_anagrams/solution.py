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
        