class Solution:
    def countOdds(self, low: int, high: int) -> int:

        if high % 2 == 0 and low % 2 == 0:
            return floor((high - low) / 2)
        return floor((high - low) / 2) + 1
