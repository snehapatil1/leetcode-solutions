class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if not length:
            return 0
        elif length == 1:
            return nums[0]
        
        current_sum = 0
        index_sum = []
        index_sum.append(nums[0])
        for ele in range(1, length):
            current_sum = index_sum[ele-1] + nums[ele]
            if current_sum > nums[ele]:
                index_sum.append(current_sum)
            else:
                index_sum.append(nums[ele])
            
        return max(index_sum)
