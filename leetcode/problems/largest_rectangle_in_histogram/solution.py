class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = -float('inf')

        for idx, height in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= height:
                prevHeight = heights[stack.pop()]
                width = idx if not stack else (idx - 1) - stack[-1]
                maxArea = max(maxArea, prevHeight * width)

            stack.append(idx)
        
        return maxArea if maxArea != -float('inf') else 0