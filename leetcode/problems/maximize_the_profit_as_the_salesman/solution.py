class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda x:x[0])
        goldMap = [0] * (n + 1)
        hashmap = [[] for _ in range(n)]
        
        for buyer in offers:
            start, end, gold = buyer[0], buyer[1], buyer[2]
            hashmap[end].append([start, gold])
        
        for end in range(1, n + 1):
            goldMap[end] = goldMap[end - 1]
            for start, gold in hashmap[end - 1]:
                goldMap[end] = max(goldMap[end], goldMap[start] + gold)
            
        return goldMap[-1]