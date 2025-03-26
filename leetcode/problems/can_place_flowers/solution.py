class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        count = 0
        for idx in range(size):
            if flowerbed[idx] == 0:
                left = (idx == 0) or (flowerbed[idx - 1] == 0)
                right = (idx == size - 1) or (flowerbed[idx + 1] == 0)
                if left and right:
                    flowerbed[idx] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n