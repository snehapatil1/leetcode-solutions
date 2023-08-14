class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minHeap = []
        curTime = 0
        output  = [] 
        # sort the tasks and store their previous index
        tasks = sorted((task, idx) for idx, task in enumerate(tasks))
        
        for (enqueueTime, processingTime), idx in tasks:
            # if there are pending tasks in heap and current time < this task enqueue time then add this task in heap
            while minHeap and curTime < enqueueTime:
                pTime, jIdx, eTime = heappop(minHeap)
                curTime = max(eTime, curTime) + pTime
                output.append(jIdx)
            # add processing time and index in heap so thta heap auto sorts it based on processign time and then index
            heappush(minHeap, (processingTime, idx, enqueueTime))
        
        return output + [idx for _, idx, _ in sorted(minHeap)]