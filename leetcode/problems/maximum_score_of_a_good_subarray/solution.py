class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        output = nums[k]
        left = right = k
        minSoFar = nums[k]

        while left > 0 or right < len(nums) - 1:
            if left == 0 or (right < len(nums) - 1 and nums[right + 1] > nums[left - 1]):
                right += 1
            else:
                left -= 1
            minSoFar = min(minSoFar, nums[left], nums[right])
            output = max(output, minSoFar * (right - left + 1))
        
        return output