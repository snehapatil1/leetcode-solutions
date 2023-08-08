class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        volume = 0

        while left < right:
            if height[left] <= height[right]:
                volume = max(volume, height[left] * (right - left))
                left += 1
            else:
                volume = max(volume, height[right] * (right - left))
                right -=1
        
        return volume