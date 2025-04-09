class Solution:
    def bfs(self, node, isConnected, visited):
        queue = deque([node])
        visited[node] = True
        while queue:
            node = queue.popleft()
            for i in range(len(isConnected)):
                if isConnected[node][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:        
        provinces = 0
        n = len(isConnected)
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                provinces += 1
                self.bfs(i, isConnected, visited)

        return provinces