class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        visited = []
        prevCounter = 0
        output = []
        
        # ["1","2","prev","prev","prev"]
        for word in words:
            if word == "prev":
                if visited and len(visited) - 1 >= len(visited) - 1 - prevCounter and len(visited) - 1 - prevCounter >= 0:
                    output.append(visited[len(visited) - 1 - prevCounter])
                else:
                    output.append(-1)
                prevCounter += 1
            else:
                visited.append(int(word))
                if prevCounter:
                    prevCounter = 0
        
        return output