class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottles = numBottles
        
        while (numBottles // numExchange) > 0:
            newBottles = numBottles // numExchange
            remaining = numBottles % numExchange
            bottles += newBottles
            numBottles = newBottles + remaining
        
        return bottles