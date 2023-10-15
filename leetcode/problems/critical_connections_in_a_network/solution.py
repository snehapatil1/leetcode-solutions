class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        rank = [n] * n
        critical = []

        for src, dest in connections:
            graph[src].append(dest)
            graph[dest].append(src)
        
        def dfs(node, discovery_time, parent):
            if rank[node] == n:
                rank[node] = discovery_time
            
                for neighbor in graph[node]:
                    if neighbor != parent:
                        expected_discovery_time = discovery_time + 1
                        actual_discovery_time = dfs(neighbor, expected_discovery_time, node)
                        if actual_discovery_time >= expected_discovery_time:
                            critical.append((node, neighbor))
                        rank[node] = min(rank[node], actual_discovery_time)
            
            return rank[node]
        
        dfs(n - 1, 0, -1)

        return critical