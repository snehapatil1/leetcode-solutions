class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def fetch(find_start, left, right):
            while left <= right < n:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    if find_start:
                        if mid == left or nums[mid - 1] < nums[mid]:
                            return mid
                        right = mid - 1
                    else:
                        if mid == right or nums[mid + 1] > nums[mid]:
                            return mid
                        left = mid + 1
            return -1
        
        start = fetch(True, 0, n - 1)
        if start == -1:
            return [-1, -1]
        
        end = fetch(False, 0, n - 1)

        return [start, end]