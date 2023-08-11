class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp = [[-1,-1,-1,-1], [-1,-1,-1,-1], [-1,-1,-1,-1]]
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        n = len(coins)

        def NumberOfWays(i, amount):
            # if we have achieved amount 0 means utilized available coins
            if not amount:
                return 1
            
            # if coins are exhausted and still amount hasen't become 0
            if i == n:
                return 0
            
            # if for this coin and remaining amount we had already calculated number of ways then use that from the dp
            if dp[i][amount] != -1:
                return dp[i][amount]
            
            if coins[i] > amount:
                # if current coin value is greater than remaining amount then skip this coin and move to next coin
                dp[i][amount] = NumberOfWays(i + 1, amount)
            else:
                # if current coin value is less than remaning amount then we will utilize current coin and find number of ways also skip this coins and find number of ways
                dp[i][amount] = NumberOfWays(i, amount - coins[i]) + NumberOfWays(i + 1, amount)
            
            return dp[i][amount]
        
        return NumberOfWays(0, amount)