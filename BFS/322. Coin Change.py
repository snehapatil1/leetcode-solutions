"""
    Question:
        You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
        Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
        You may assume that you have an infinite number of each kind of coin.
"""

from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialise queue with amount and 0 coins
        queue = deque([(amount, 0)])
        # initialise seen set with amount
        seen = set([amount])

        while queue:
            # remove element from queue
            current_amount, num_coins = queue.popleft()
            # if current_amount remaining is 0 then return num_coins
            if not current_amount:
                return num_coins
            
            # evaluate each coin for current remaining amount
            for coin in coins:
                # if current coin can be used and diff is not in seen then add it in queue and seen
                if ((current_amount - coin) >= 0) and (current_amount - coin) not in seen:
                    queue.append((current_amount - coin, num_coins + 1))
                    seen.add(current_amount - coin)
        
        return -1
