class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordcount = Counter(words)
        result = []
        window = len(words[0])
        substringlength = len(words) * window
        
        for i in range(len(s) - substringlength + 1):
            substr = s[i : i + substringlength]
            substrcount = {}
            for j in range(0, len(substr), window):
                word = substr[j : j + window]
                substrcount[word] = substrcount.get(word, 0) + 1
            if substrcount == wordcount:
                result.append(i)
        
        return result