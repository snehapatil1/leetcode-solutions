class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMaxHeight, rightMaxHeight = 0, 0
        capacity = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] > leftMaxHeight:
                    leftMaxHeight = height[left]
                capacity += (leftMaxHeight - height[left])
                left += 1
            else:
                if height[right] > rightMaxHeight:
                    rightMaxHeight = height[right]
                capacity += (rightMaxHeight - height[right])
                right -= 1
        
        return capacity