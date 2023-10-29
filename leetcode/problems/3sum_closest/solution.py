class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest, minDiff = 0, float('inf')
        n = len(nums)
        for first in range(n - 2):
            second, third = first + 1, n - 1
            while second < third:
                total = nums[first] + nums[second] + nums[third]
                
                if abs(total - target) < minDiff:
                    minDiff = abs(total - target)
                    closest = total
                
                if total == target:
                    return total
                
                if total < target:
                    second += 1
                else:
                    third -= 1
        
        return closest