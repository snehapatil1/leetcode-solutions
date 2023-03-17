class Solution:
    # Backtracking Solution
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        combinations = []
        
        def backtracking(index, currentString):
            if index == len(digits):
                combinations.append(currentString)
            else:
                for letter in phone[digits[index]]:
                    backtracking(index + 1, currentString + letter)
        
        backtracking(0, '')

        return combinations
    
    ##### Brute Force Solution #####
    # def letterCombinations(self, digits: str) -> List[str]:
    #     if len(digits) == 0:
    #         return []
        
    #     numberMap = {
    #         '2': ['a', 'b', 'c'],
    #         '3': ['d', 'e', 'f'],
    #         '4': ['g', 'h', 'i'],
    #         '5': ['j', 'k', 'l'],
    #         '6': ['m', 'n', 'o'],
    #         '7': ['p', 'q', 'r', 's'],
    #         '8': ['t', 'u', 'v'],
    #         '9': ['w', 'x', 'y', 'z']
    #     }
    #     output = []
    #     digitsList = list(digits)

    #     if len(digitsList) == 1:
    #         return numberMap[digitsList[0]]
        
    #     numberOfCombinations = 1
    #     for i in range(len(digitsList)):
    #         numberOfCombinations = numberOfCombinations * len(numberMap[digitsList[i]])
        
    #     for digit in digitsList[:1]:
    #         for lt in numberMap[digit]:
    #             for i in range(numberOfCombinations):
    #                 output.append(lt)
        
    #     for digit in digitsList[1:]:
    #         lettersCount = len(numberMap[digit])
    #         alteriby = 0
    #         for lt in numberMap[digit]:
    #             i = 0 + alteriby
    #             while i < len(output):
    #                 originalString = output[i]
    #                 newString = originalString + lt
    #                 output[i] = newString
    #                 i += lettersCount
    #             alteriby += 1
    #         output.sort()
        
    #     return set(output)
