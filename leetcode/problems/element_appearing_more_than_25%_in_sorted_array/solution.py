class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # ===== Hash Map =====
        # count = defaultdict(int)
        # n = len(arr)
        # target = n / 4
        # for val in arr:
        #     count[val] = count.get(val, 0) + 1
        #     if count[val] > target:
        #         return val 
        # return -1

        # ===== Array Math =====
        # n = len(arr)
        # target = n // 4
        # for idx in range(n - target):
        #     if arr[idx] == arr[idx + target]:
        #         return arr[idx]   
        # return -1

        # ===== Binary Search =====
        n = len(arr)
        target = n / 4
        nums = [arr[n // 4], arr[n // 2], arr[3 * n // 4]]
        for num in nums:
            left = bisect_left(arr, num)
            right = bisect_right(arr, num) - 1
            if right - left + 1 > target:
                return num
        return -1