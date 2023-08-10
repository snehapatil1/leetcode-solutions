class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums_set = list(set(nums))
        left = 0
        right = len(nums_set) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums_set[mid] == target:
                return True
            elif nums_set[left] <= nums_set[mid]:
                if nums_set[left] <= target < nums_set[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums_set[mid] <= target < nums_set[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False