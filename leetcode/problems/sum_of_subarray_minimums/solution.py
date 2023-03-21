class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        dp = [0] * len(arr)
        stack = []
        start, end = 0, len(arr)
        
        while start < end:
            while stack and arr[stack[-1]] >= arr[start]:
                # remove elements from stack until current numebr is >= stack element
                stack.pop()
            if stack:
                j = stack[-1]
                dp[start] = dp[j] + (start - j) * arr[start]
            else:
                dp[start] = (start + 1) * arr[start]
            stack.append(start)
            start += 1
        
        return sum(dp) % ((10**9) + 7)