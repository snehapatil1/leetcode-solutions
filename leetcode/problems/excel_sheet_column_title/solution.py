class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        x = (columnNumber-1) % 26
        rest = (columnNumber-1) // 26
        
        if (rest == 0):
            return digits[x]
        return self.convertToTitle(rest) + digits[x]