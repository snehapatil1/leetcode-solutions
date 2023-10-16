class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        output = 0
        charsMap = Counter(chars)
        
        for word in words:
            availableChars = {key:charsMap[key] for key in charsMap}
            skip = False
            for ch in word:
                if availableChars.get(ch, 0) > 0:
                    availableChars[ch] -= 1
                else:
                    skip = True
                    break
            if not skip:
                output += len(word)
        
        return output