class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.getLeftIndex(nums, target)
        right = self.getRightIndex(nums, target)

        return [left, right]
    
    def getLeftIndex(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target and mid - 1 >= 0 :
                    return mid
                else:
                    right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    def getRightIndex(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target and mid + 1 <= len(nums) - 1 :
                    return mid
                else:
                    left = mid + 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1