class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = []
        
        for i in range(rowIndex + 1):
            if(i == 0):
                prev = [1]
                output.append(prev)
            else:
                curr = [1]
                j = 1
                while(j < i):
                    curr.append(prev[j-1] + prev[j])
                    j+=1
                curr.append(1)
                output.append(curr)
                prev = curr
        
        return output[rowIndex]
