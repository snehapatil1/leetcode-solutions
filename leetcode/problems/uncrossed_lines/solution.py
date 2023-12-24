class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for idx1 in range(1, n1 + 1):
            for idx2 in range(1, n2 + 1):
                if nums1[idx1 - 1] == nums2[idx2 - 1]:
                    dp[idx1][idx2] = dp[idx1 - 1][idx2 - 1] + 1
                else:
                    dp[idx1][idx2] = max(dp[idx1][idx2 - 1], dp[idx1 - 1][idx2])
        
        return dp[n1][n2]