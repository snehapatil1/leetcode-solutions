class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFrequency = 0
        left, curr = 0, 0

        for right in range(len(nums)):
            target = nums[right]
            curr += target
            
            while (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1
            
            maxFrequency = max(maxFrequency, right - left + 1)
        
        return maxFrequency