class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        gNum = ""

        l, r = 0, 2
        while l <= n - 3:
            if num[l] == num[l + 1] == num[l + 2]:
                if (gNum and int(num[l] + num[l + 1] + num[l + 2]) > int(gNum)) or (not gNum):
                    gNum = num[l] + num[l + 1] + num[l + 2]
            l += 1
            r += 1
    
        return gNum