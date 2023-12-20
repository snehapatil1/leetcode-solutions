class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # prices.sort()
        # return money - (prices[0] + prices[1]) if prices[0] + prices[1] <= money else money

        def getMinIndex(prices):
            minIndex = 0

            for idx in range(1, len(prices)):
                if prices[idx] < prices[minIndex]:
                    minIndex = idx
            return minIndex
        
        minIndex = getMinIndex(prices)
        minCost = prices.pop(minIndex)
        secondMinIndex = getMinIndex(prices)
        minCost += prices[secondMinIndex]

        return money - minCost if minCost <= money else money