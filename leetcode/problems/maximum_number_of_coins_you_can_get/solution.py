class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # piles.sort()
        # myValue = 0

        # for idx in range(len(piles) // 3, len(piles), 2):
        #     myValue += piles[idx]

        # return myValue

        piles.sort()
        queue = deque(piles)
        myValue = 0

        while queue:
            queue.pop()
            myValue += queue.pop()
            queue.popleft()
        
        return myValue