class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = Counter(nums)
        output = 0

        for num in count:
            if count[num] > 2:
                k = count[num] - 2
                output += 2
                while k > 0:
                    nums.remove(num)
                    # nums.append('_')
                    k -= 1
            else:
                output += count[num]
        
        return output