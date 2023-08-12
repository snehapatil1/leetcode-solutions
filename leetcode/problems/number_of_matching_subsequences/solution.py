class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        countMap = {}

        counter = collections.Counter(words)
        words = set(words)
        for target in words:
            print(target)
            if set(target) - set(s):
                continue
            
            sidx, tidx = 0, 0

            isSubsequence = False
            while tidx < len(target):
                if sidx == len(s):
                    isSubsequence = False
                    break
                if target[tidx] == s[sidx]:
                    isSubsequence = True
                    tidx += 1
                sidx += 1
            
            if isSubsequence:
                count += 1
                if target not in countMap.keys():
                    countMap.update({ target:count })
        
        finalcount = count
        print(countMap)
        for cnt in countMap.keys():
            finalcount += counter[cnt] - 1
        return finalcount