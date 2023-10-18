class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for src, dest in relations:
            graph[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1
        
        queue = deque([])
        maxTime = [0] * (n + 1)
        for i in range(1, n + 1):
            if indegree.get(i, 0) == 0:
                queue.append(i)
                maxTime[i] = time[i - 1]
        
        while queue:
            course = queue.popleft()
            for nextC in graph[course]:
                maxTime[nextC] = max(maxTime[nextC], maxTime[course] + time[nextC - 1])
                indegree[nextC] -= 1
                if indegree[nextC] == 0:
                    queue.append(nextC)
        
        return max(maxTime)