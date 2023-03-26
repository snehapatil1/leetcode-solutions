class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        l = len(nums)
        left_product = [0] * l
        left_product[0] = 1
        right_product = [0] * l
        right_product[l - 1] = 1

        for idx in range(1, l):
            left_product[idx] = nums[idx - 1] * left_product[idx - 1]
        for idx in reversed(range(0, l - 1)):
            right_product[idx] = nums[idx + 1] * right_product[idx + 1]

        for i in range(l):
            output.append(left_product[i] * right_product[i])

        return output
