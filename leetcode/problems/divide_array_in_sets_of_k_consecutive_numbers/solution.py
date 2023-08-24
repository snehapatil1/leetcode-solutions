class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        if n % k:
            return False
        
        nums.sort()
        count = collections.Counter(nums)
        
        for idx in range(n):
            if not count[nums[idx]]:
                continue
            for j in range(nums[idx], nums[idx] + k):
                if count[j] > 0:
                    count[j] -= 1
                else:
                    return False

        return True