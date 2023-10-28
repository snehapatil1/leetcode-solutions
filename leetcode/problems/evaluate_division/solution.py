class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for idx in range(len(equations)):
            src, dest = equations[idx]
            weight = values[idx]
            graph[src].append((dest, weight))
            graph[dest].append((src, 1 / weight))
        
        output = []
        def dfs(src, dest, visited, value):
            if src not in graph or dest not in graph or src in visited:
                return -1
            
            if src == dest:
                return value
            
            visited.add(src)
            for dt, val in graph[src]:
                product = dfs(dt, dest, visited, value * val)
                if product != -1:
                    return product
            
            return -1
        
        for src, dest in queries:
            val = dfs(src, dest, set(), 1)
            output.append(val)
        
        return output