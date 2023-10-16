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

        # cnt = collections.Counter(s1)
        
        # left = 0
        # for right, ch in enumerate(s2):
        #     cnt[ch] -= 1
        #     while cnt[ch] < 0:
        #         cnt[s2[left]] += 1
        #         left += 1
        #     if right - left + 1 == len(s1):
        #         return True
            
        # return False

        s1map = Counter(s1)
        n = len(s1)

        for i in range(len(s2)):
            if s2[i] in s1map:
                s1map[s2[i]] -= 1
            if i >= n and s2[i - n] in s1map:
                s1map[s2[i - n]] += 1
            
            if all([s1map[x] == 0 for x in s1map]):
                return True
        
        return False