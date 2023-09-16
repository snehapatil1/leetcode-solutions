class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(dict)

        for node1, node2 in edges:
            graph[node1][node2] = 0
            graph[node2][node1] = 1
        
        @cache
        def dfs(i, j):
            return sum([(dfs(j, k) + graph[j][k]) for k in graph[j] if k != i])
        
        dp = [-1] * n
        for x in range(n):
            dp[x] = dfs(-1, x)
        return dp