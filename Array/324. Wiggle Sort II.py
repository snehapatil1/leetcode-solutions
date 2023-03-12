class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        k = (len(nums) + 1) // 2
        arr1 = nums[:k]
        arr2 = nums[k:]
        arr1.reverse()
        arr2.reverse()
        arr1_pointer = 0
        arr2_pointer = 0

        print(arr1, arr2)
        for i in range(len(nums)):
            if i%2 == 0:
                nums[i] = arr1[arr1_pointer]
                arr1_pointer += 1
            else:
                nums[i] = arr2[arr2_pointer]
                arr2_pointer += 1
