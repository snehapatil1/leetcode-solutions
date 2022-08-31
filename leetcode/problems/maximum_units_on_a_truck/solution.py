class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        # print(boxTypes)
        availableSize = truckSize
        unitsAdded = 0
        
        for box in boxTypes:
            if (not availableSize):
                break
            boxesToAdd = availableSize if box[0] > availableSize else box[0]
            unitsAdded += (boxesToAdd * box[1])
            availableSize -= boxesToAdd
            # print(boxesToAdd, unitsAdded, availableSize)
        
        return unitsAdded
                