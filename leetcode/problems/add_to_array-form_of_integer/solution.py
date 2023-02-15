class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        newNum = [str(n) for n in num]
        number = int("".join(newNum))
        numSum = number + k
        numSumString = str(numSum)
        numSumStringArr = list(numSumString)
        outputArr = [int(i) for i in numSumStringArr]
        return outputArr