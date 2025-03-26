class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        result = [False] * n
        maxCandies = max(candies)
        for kid in range(n):
            if (candies[kid] + extraCandies) >= maxCandies:
                result[kid] = True

        return result