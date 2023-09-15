class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        for node1, node2 in edges:
            indegree[node1] = indegree.get(node1, 0) + 1
            indegree[node2] = indegree.get(node2, 0) + 1
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        queue = deque([node for node, cnt in indegree.items() if cnt == 1])
        while queue:
            node = queue.popleft()
            indegree[node] -= 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 1:
                    queue.append(neighbor)
        for node1, node2 in edges[::-1]:
            if indegree[node1] == 2 and indegree[node2]:
                return [node1, node2]
        return []