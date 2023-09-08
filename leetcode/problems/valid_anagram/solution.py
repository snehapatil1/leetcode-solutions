class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_arr = list(s)
        # t_arr = list(t)
        # s_arr.sort()
        # t_arr.sort()

        # return s_arr == t_arr

        # return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False
        
        countS, countT = defaultdict(int), defaultdict(int)

        for idx in range(len(s)):
            countS[s[idx]] = countS.get(s[idx], 0) + 1
            countT[t[idx]] = countT.get(t[idx], 0) + 1
        
        return countS == countT