class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2:
            return False
        target = totalSum // 2
        dp = set()
        dp.add(0)

        curSum = 0
        for idx in range(len(nums) - 1, -1, -1):
            nextDp = set()
            for t in dp:
                if (t + nums[idx]) == target:
                    return True
                nextDp.add(t + nums[idx])
                nextDp.add(t)
            dp = nextDp
        return False