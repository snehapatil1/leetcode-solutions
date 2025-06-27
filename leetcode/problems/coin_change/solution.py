class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([(amount, 0)])
        seen = set([amount])

        while queue:
            curr_amount, curr_coins = queue.popleft()
            if curr_amount == 0:
                return curr_coins
            
            for coin in coins:
                if (curr_amount - coin) >= 0 and (curr_amount - coin) not in seen:
                    seen.add(curr_amount - coin)
                    queue.append((curr_amount - coin, curr_coins + 1))

        return -1