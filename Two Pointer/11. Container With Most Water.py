"""
    Question:
        You are given an integer array height of length n. 
        There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
        Find two lines that together with the x-axis form a container, such that the container contains the most water.
        Return the maximum amount of water a container can store.
        Notice that you may not slant the container.
"""

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
