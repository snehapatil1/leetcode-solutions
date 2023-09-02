class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # temp = list(s1)
        # temp[0], temp[2] = s1[2], s1[0]
        
        # if s1 == s2:
        #     return True
        
        # if ''.join(temp) == s2:
        #     return True
        
        # temp = list(s1)
        # temp[1], temp[3] = s1[3], s1[1]
        # if ''.join(temp) == s2:
        #     return True
        
        # temp = list(s1)
        # temp[0], temp[2] = s1[2], s1[0]
        # temp[1], temp[3] = s1[3], s1[1]
        # if ''.join(temp) == s2:
        #     return True
        
        # return False

        return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2])        
        