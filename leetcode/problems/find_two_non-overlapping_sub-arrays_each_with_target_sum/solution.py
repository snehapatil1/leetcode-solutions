class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        left, res = 0, float('inf')
        dp = [float('inf')] * len(arr)
        window_sum = 0

        for right, num in enumerate(arr):
            window_sum += num
            while window_sum > target:
                window_sum -= arr[left]
                left += 1
            if window_sum == target:
                cur_len = right - left + 1
                res = min(res, cur_len + dp[left - 1])
                dp[right] = min(dp[right - 1], cur_len)
            else:
                dp[right] = dp[right - 1]
        return res if res < float('inf') else -1