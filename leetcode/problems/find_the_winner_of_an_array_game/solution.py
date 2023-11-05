class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k > n:
            return max(arr)
        
        counter = 0
        currNum = float('inf')

        while True:
            if arr[0] > arr[1]:
                num = arr[1]
                arr.pop(1)
                arr.append(num)
                if arr[0] != currNum:
                    counter = 0
                currNum = arr[0]
                counter += 1
            else:
                num = arr[0]
                if arr[1] != currNum:
                    counter = 0
                currNum = arr[1]
                counter += 1
                arr.pop(0)
                arr.append(num)
            
            if counter >= k:
                return currNum