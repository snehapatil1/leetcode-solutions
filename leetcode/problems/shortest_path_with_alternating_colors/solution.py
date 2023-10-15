class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        output = [-1] * n
        graph = defaultdict(list)

        for src, dest in redEdges:
            graph[src].append((dest, 0))
        
        for src, dest in blueEdges:
            graph[src].append((dest, 1))
        
        queue = deque([(0, 0, -1)])
        visited = [[False, False] for i in range(n)]
        visited[0][0] = visited[0][1] = True
        output[0] = 0

        while queue:
            node, steps, prevcolor = queue.popleft()
            for neighbor, color in graph[node]:
                if color != prevcolor and not visited[neighbor][color]:
                    visited[neighbor][color] = True
                    queue.append((neighbor, steps + 1, color))
                    if output[neighbor] == -1:
                        output[neighbor] = steps + 1
        
        return output