class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Using Topological Sorting - Kahn's Algorithm
        adjacency_list = collections.defaultdict(list)
        indegree = {}
        
        for dest, src in prerequisites:
            adjacency_list[src].append(dest)
            if dest not in indegree.keys():
                indegree.update({ dest: 0 })
            indegree[dest] += 1
        
        queue = collections.deque([k for k in range(numCourses) if k not in indegree])
        courses_order = []

        while queue:
            course = queue.popleft()
            courses_order.append(course)
            if course in adjacency_list:
                for dependent_course in adjacency_list[course]:
                    indegree[dependent_course] -= 1
                    if not indegree[dependent_course]:
                        queue.append(dependent_course)
        return courses_order if len(courses_order) == numCourses else []
