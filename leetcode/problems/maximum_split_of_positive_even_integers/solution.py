class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        
        output = []
        factor = 2

        while factor <= finalSum:
            output.append(factor)
            finalSum -= factor
            factor += 2
        
        output[-1] += finalSum
        
        return output