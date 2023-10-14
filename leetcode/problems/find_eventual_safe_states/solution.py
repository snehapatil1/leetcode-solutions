class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        safe = [False] * n

        while queue:
            node = queue.popleft()
            safe[node] = True

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        safeNodes = []
        for i in range(n):
            if safe[i]:
                safeNodes.append(i)
        
        return safeNodes