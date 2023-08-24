import heapq
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        ans = [-1] * len(tasks)
        servers_heap, unavailable = [], []
        queue = collections.deque()

        for idx, weight in enumerate(servers):
            heapq.heappush(servers_heap, (weight, idx))
        
        queue.append(0)

        timer = 0
        while queue and timer < len(tasks):
            task_idx = queue.popleft()
            while unavailable and unavailable[0][0] == timer:
                _, weight, server_index = heapq.heappop(unavailable)
                heapq.heappush(servers_heap, (servers[server_index], server_index))
            
            if len(servers_heap) > 0:
                server_weight, server_index = heapq.heappop(servers_heap)
                heapq.heappush(unavailable, (timer + tasks[task_idx], server_weight, server_index))
                ans[task_idx] = server_index
            else:
                finish_time, weight, id = heapq.heappop(unavailable)
                heapq.heappush(unavailable, (finish_time + tasks[task_idx], weight, id))
                ans[task_idx] = id
            
            timer += 1
            queue.append(timer)
        
        return ans