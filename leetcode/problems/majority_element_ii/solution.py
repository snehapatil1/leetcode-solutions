class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) / 3
        countMap = defaultdict(int)
        output = []

        for num in nums:
            if num not in output:
                countMap[num] = countMap.get(num, 0) + 1
                if countMap[num] > n:
                    output.append(num)
        
        return output

        # if not nums:
        #     return []
        
        # candidate1, candidate2, count1, count2 = 0, 1, 0, 0

        # for num in nums:
        #     if num == candidate1:
        #         count1 += 1
        #     elif num == candidate2:
        #         count2 += 1
        #     elif count1 == 0:
        #         candidate1, count1 = num, 1
        #     elif count2 == 0:
        #         candidate2, count2 = num, 1
        #     else:
        #         count1, count2 = count1 - 1, count2 - 1
        
        # return [num for num in [candidate1, candidate2] if nums.count(num) > len(nums) // 3]