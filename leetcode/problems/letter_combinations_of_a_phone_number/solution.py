class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        output = []

        def backtrack(i, curr):
            if len(curr) == len(digits):
                output.append("".join(curr))
                return
            
            for lt in mapping[digits[i]]:
                curr.append(lt)
                backtrack(i + 1, curr)
                curr.pop()
        
        backtrack(0, [])

        return output