class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        countMap = defaultdict(int)
        goodPairs = 0
        
        for num in nums:
            if num in countMap:
                goodPairs += countMap[num]
            
            countMap[num] = countMap.get(num, 0) + 1
        
        return goodPairs