class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = [False] * len(l)
        for idx in range(len(l)):
            arr = nums[l[idx] : r[idx] + 1]
            arr.sort()
            diff = arr[1] - arr[0]
            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    output[idx] = False
                    break
            else:
                output[idx] = True
        
        return output