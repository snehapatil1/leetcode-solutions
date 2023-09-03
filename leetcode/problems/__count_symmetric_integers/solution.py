class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        
        for i in range(low, high + 1):
            istr = str(i)
            if len(istr) % 2 == 0:
                half = len(istr) // 2
                part1Sum = sum([int(x) for x in istr[:half]])
                part2Sum = sum([int(x) for x in istr[half:]])
                if part1Sum == part2Sum:
                    count += 1
        return count