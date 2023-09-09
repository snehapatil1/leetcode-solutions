class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None)
        def combinations(target):
            if target == 0:
                return 1
            
            result = 0
            for num in nums:
                if target - num >= 0:
                    result += combinations(target - num)
            return result
        
        return combinations(target)