class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        time = 0
        counter = 0
        for processor in processorTime:
            time = max(time, processor + tasks[counter])
            counter += 4
        
        return time