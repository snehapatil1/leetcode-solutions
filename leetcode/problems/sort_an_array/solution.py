class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])
            return merge(left, right)
        
        def merge(left, right):
            left_pointer, right_pointer = 0, 0
            sorted_list = []
            while left_pointer < len(left) and right_pointer < len(right):
                if left[left_pointer] <= right[right_pointer]:
                    sorted_list.append(left[left_pointer])
                    left_pointer += 1
                else:
                    sorted_list.append(right[right_pointer])
                    right_pointer += 1
            sorted_list.extend(left[left_pointer:])
            sorted_list.extend(right[right_pointer:])
            return sorted_list
        
        return mergesort(nums)