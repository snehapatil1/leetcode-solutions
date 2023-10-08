class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        def twoSum(nums, target):
            output = []
            visited = set()

            for i in range(len(nums)):
                if len(output) == 0 or output[-1][1] != nums[i]:
                    if target - nums[i] in visited:
                        output.append([target - nums[i], nums[i]])
                visited.add(nums[i])
            
            return output
        
        def nSum(nums, target, n):
            output = []
            if not nums:
                return output
            
            if n == 2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in nSum(nums[i + 1:], target - nums[i], n - 1):
                        output.append([nums[i]] + subset)
            
            return output
        
        return nSum(nums, target, 4)