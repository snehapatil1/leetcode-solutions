class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @lru_cache(n)
        def dp(index):
            if index == n - 1:
                return True
            
            if nums[index] == 0:
                return False
            
            for i in range(index + 1, min(index + nums[index], n - 1) + 1):
                if dp(i):
                    return True
            
            return False
        
        return dp(0)