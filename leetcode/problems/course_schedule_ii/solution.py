class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        output = []

        for idx in range(len(prerequisites)):
            c2, c1 = prerequisites[idx]
            indegree[c2] += 1
            adj[c1].append(c2)
        
        queue = deque()
        for idx in range(numCourses):
            if indegree[idx] == 0:
                queue.append(idx)
        
        while queue:
            course = queue.popleft()
            output.append(course)
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return output if len(output) == numCourses else []