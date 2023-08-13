class Solution:

    def __init__(self, nums: List[int]):
        self.original_nums = nums
        self.nums = nums

    def reset(self) -> List[int]:
        self.nums = self.original_nums
        return self.nums

    def shuffle(self) -> List[int]:
        arr = []
        visited = set()
        while len(arr) < len(self.original_nums):
            num = random.choice(list(set(self.original_nums)-visited))
            if num not in arr:
                arr.append(num)
                visited.add(num)
        
        return arr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()