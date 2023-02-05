class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        word = list(word)

        commonString = ""
        currentString = ""
        for alp in word:
            currentString += alp
            for wd in strs[1:]:
                if not wd.startswith(currentString):
                    return commonString
            commonString += alp
            
        return commonString