"""
	Question:
		Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
		The overall run time complexity should be O(log (m+n)).
"""
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
