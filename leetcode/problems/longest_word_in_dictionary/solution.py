class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        hash_map = set()
        output = ""
        hash_map.add("")
        
        for word in words:
            if word[:-1] in hash_map:
                if len(word) > len(output):
                    output = word
                hash_map.add(word)
        
        return output