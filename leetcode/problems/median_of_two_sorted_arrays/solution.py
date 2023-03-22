class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        nums1.sort()
        n = len(nums1)
        if n % 2 == 0:
            mid = n // 2
            return (nums1[mid] + nums1[mid - 1]) / 2
        else:
            mid = n // 2
            return nums1[mid]