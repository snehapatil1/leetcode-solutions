class Solution:
    def largestOddNumber(self, num: str) -> str:
        for idx in range(len(num) - 1, -1, -1):
            if int(num[idx]) % 2:
                return num[:idx + 1]

        return ""