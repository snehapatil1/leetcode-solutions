class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        max_operations = 0
        complement_map = defaultdict(int)
        
        for num in nums:
            complement = k - num
            if complement in complement_map and complement_map[complement]:
                max_operations += 1
                complement_map[complement] -= 1
            else:
                complement_map[num] = complement_map.get(num, 0) + 1
        
        return max_operations