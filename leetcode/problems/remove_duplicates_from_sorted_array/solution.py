class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = Counter(nums)

        for num in count:
            if count[num] > 1:
                k = count[num] - 1
                while k > 0:
                    nums.remove(num)
                    nums.append('_')
                    k -= 1
        
        return len(count)