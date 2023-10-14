class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        
        provinces = 0
        graph = defaultdict(list)
        queue = deque([])
        n = len(isConnected)

        for i in range(n):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]:
                    graph[i].append(j)
        
        visited = set()
        for node in range(n):
            if node not in visited:
                queue.append(node)
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(node)
                            queue.append(neighbor)
                provinces += 1

        return provinces