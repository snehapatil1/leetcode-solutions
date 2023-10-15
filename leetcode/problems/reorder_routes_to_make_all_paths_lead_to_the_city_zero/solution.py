class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        count = 0
        visited = [False] * n
        graph = defaultdict(list)
        for src, dest in connections:
            graph[src].append((dest, 1))
            graph[dest].append((src, 0))
        
        queue = deque([0])
        visited[0] = True

        while queue:
            node = queue.popleft()
            for neighbor, sign in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    count += sign
                    queue.append((neighbor))
        
        return count