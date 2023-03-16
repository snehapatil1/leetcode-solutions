class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        value_map = {num: -1 for num in nums2}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                value_map[stack.pop()] = num
            stack.append(num)

        for num in nums1:
            output.append(value_map[num])
        
        return output
