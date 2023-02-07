class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = 0
        digitsLen = len(digits)

        for idx, ele in enumerate(digits):
            integer += (ele * (10** (digitsLen - (idx + 1))))
        
        newInteger = integer + 1

        newIntegerString = str(newInteger)

        newList = list(newIntegerString)

        finalList = []
        
        for ele in newList:
            finalList.append(int(ele))

        return finalList
