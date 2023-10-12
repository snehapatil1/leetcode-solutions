# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        mountainLen = mountain_arr.length()

        def getPeakIndex(start, end):
            while start < end:
                mid = (start + end) // 2
                midValue = mountain_arr.get(mid)
                rightValue = mountain_arr.get(mid + 1)
                if midValue < rightValue:
                    start = mid + 1
                else:
                    end = mid
            return start

        def searchLeft(start, end):
            while start != end:
                mid = (start + end) // 2
                midValue = mountain_arr.get(mid)
                if target > midValue:
                    start = mid + 1
                else:
                    end = mid

            return start if mountain_arr.get(start) == target else -1
        
        def searchRight(start, end):
            while start != end:
                mid = (start + end) // 2
                midValue = mountain_arr.get(mid)
                if target < midValue:
                    start = mid + 1
                else:
                    end = mid
            
            return start if mountain_arr.get(start) == target else -1
        
        peakIndex = getPeakIndex(1, mountainLen - 1 - 2)
        
        targetIndex = searchLeft(0, peakIndex)
        if targetIndex != -1:
            return targetIndex
        
        targetIndex = searchRight(peakIndex + 1, mountainLen - 1)
        if targetIndex != -1:
            return targetIndex
        
        return -1
