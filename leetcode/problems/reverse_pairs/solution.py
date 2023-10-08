class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n, count = len(nums), 0

        def mergeSort(left, right):
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            count = mergeSort(left, mid) + mergeSort(mid + 1, right)
            p1, p2 = left, mid + 1

            while p1 <= mid and p2 <= right:
                if nums[p1] > (2 * nums[p2]):
                    count += mid - p1 + 1
                    p2 += 1
                else:
                    p1 += 1
            nums[left : right + 1] = sorted(nums[left : right + 1])

            return count
        
        return mergeSort(0, n - 1)
            


        
