"""
    Question:
        You are given a sorted array consisting of only integers where every element appears exactly twice, 
        except for one element which appears exactly once.
        Return the single element that appears only once.
        Your solution must run in O(log n) time and O(1) space.
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if (mid % 2 == 0 and nums[mid] == nums[mid - 1]) or (mid % 2 != 0 and nums[mid] == nums[mid + 1]):
                right = mid - 1
            else:
                left = mid + 1
            
        return nums[left - 1]
