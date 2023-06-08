"""
    Question:
        You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
        The digits are ordered from most significant to least significant in left-to-right order. 
        The large integer does not contain any leading 0's.
        Increment the large integer by one and return the resulting array of digits.
"""

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
