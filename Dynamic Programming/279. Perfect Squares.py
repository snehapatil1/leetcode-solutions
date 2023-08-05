"""
    Question:
        Given an integer n, return the least number of perfect square numbers that sum to n.
        A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. 
        For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
"""

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        i = 1
        while i < n + 1:
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
            i += 1
        
        return dp[-1]
