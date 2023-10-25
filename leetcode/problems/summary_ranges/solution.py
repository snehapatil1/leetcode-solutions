class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        start, end, n = 0, 0, len(nums)

        while start < n and end < n:
            if (end + 1) < n and (nums[end] + 1) == nums[end + 1]:
                end += 1
            else:
                if nums[start] == nums[end]:
                    output.append(f"{nums[start]}")
                    start += 1
                    end += 1
                else:
                    output.append(f"{nums[start]}->{nums[end]}")
                    end += 1
                    start = end
        return output