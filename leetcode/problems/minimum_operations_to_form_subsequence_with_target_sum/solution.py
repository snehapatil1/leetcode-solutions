class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if total_sum < target:
            return -1
        
        operations = 0
        nums.sort()
        
        while target:
            num = nums.pop(-1)
            if total_sum - num >= target:
                total_sum -= num
            elif num <= target:
                total_sum -= num
                target -= num
            else:
                nums.append(num / 2)
                nums.append(num / 2)
                operations += 1
        return operations
            
            