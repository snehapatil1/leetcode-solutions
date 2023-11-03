class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ptr = 0
        output = []

        for num in range(1, n + 1):
            if ptr >= len(target):
                break
            if target[ptr] == num:
                output.append("Push")
                ptr += 1
            else:
                output.append("Push")
                output.append("Pop")
        
        return output