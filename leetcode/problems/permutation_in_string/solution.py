class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 = sorted(s1)
        # p1, p2 = 0, len(s1) - 1
        
        # while p1 < (len(s2) - len(s1) + 1) and p2 < len(s2):
        #     substring = s2[p1: p2 + 1]
        #     substring = sorted(substring)
        #     if substring == s1:
        #         return True
        #     p1 += 1
        #     p2 += 1
        
        # return False

        cnt = collections.Counter(s1)
        
        l = 0
        for r, c in enumerate(s2):
            cnt[c] -= 1
            while cnt[c] < 0:
                cnt[s2[l]] += 1
                l += 1
            if r - l + 1 == len(s1):
                return True
            
        return False