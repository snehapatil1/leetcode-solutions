class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        nmod = {}

        for num in time:
            mod = num % 60
            if mod == 0:
                if 0 in nmod.keys():
                    count += nmod[0]
            elif (60 - mod) in nmod.keys():
                count += nmod[60 - mod]
            
            if mod in nmod.keys():
                nmod[mod] += 1
            else:
                nmod[mod] = 1
        
        return count
