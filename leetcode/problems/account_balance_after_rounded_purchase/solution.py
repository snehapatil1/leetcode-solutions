import math
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount < 5:
            amount = 0
        elif purchaseAmount == 5:
            amount = 10
        elif purchaseAmount%10 < 5:
            amount = round(purchaseAmount/10) * 10
        else:
            amount = math.ceil(purchaseAmount/10) * 10
        return 100 - amount