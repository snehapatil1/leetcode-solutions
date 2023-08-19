class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # maintain how many times are left for selling stocks in k
        # maintain if current you are holding a stock or not
        holding = 0
        no_of_days = len(prices)
        
        @lru_cache(None)
        def get_maximum_profit(day, transactions_remaining, holding):
            if transactions_remaining == 0 or day == no_of_days:
                return 0

            # on each day, you can either do something with the stock or do nothing
            do_nothing = get_maximum_profit(day + 1, transactions_remaining, holding)
            do_something = 0

            # for doing something with the stock there are 2 options - 
            if not holding:
                # 1. if you are not holding stock then buy - Buy stocks
                do_something = -prices[day] + get_maximum_profit(day + 1, transactions_remaining, 1)
            else:
                # 2. if you are holding stock then sell - Sell stocks
                do_something = prices[day] + get_maximum_profit(day + 1, transactions_remaining - 1, 0)
        
            return max(do_nothing, do_something)
        
        return get_maximum_profit(0, k, 0)