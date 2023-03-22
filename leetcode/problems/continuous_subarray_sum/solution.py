class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        if sum(nums) % k == 0:
            return True
        
        hm = {0:-1}
        current_sum = 0

        for idx in range(n):
            current_sum = (current_sum + nums[idx]) % k
            if current_sum not in hm:
                hm[current_sum] = idx
            else:
                if idx - hm[current_sum] > 1:
                    return True
        return False