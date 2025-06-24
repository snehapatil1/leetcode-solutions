class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left, right = 0, len(height) - 1

        while left < right:
            volume = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, volume)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water