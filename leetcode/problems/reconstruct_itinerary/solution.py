class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort()
        for src, dest in tickets:
            graph[src].append(dest)
        
        path = ["JFK"]

        def dfs(src):
            if len(path) == len(tickets) + 1:
                return path
            if src not in graph:
                return False
            
            temp = list(graph[src])
            for idx, dest in enumerate(temp):
                graph[src].pop(idx)
                path.append(dest)
                if dfs(dest):
                    return True
                graph[src].insert(idx, dest)
                path.pop()
            return False
        
        dfs("JFK")
        return path