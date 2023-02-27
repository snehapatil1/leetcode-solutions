import heapq
# heap.heapify(arr) -> constructs heap (tree)
# heap.heappush(arr, ele) -> adds element in heap and restructures heap tree
# heap.heappop(arr) -> deletes top element from heap and restructures heap tree

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # if there are no meetings then 0 rooms required
        if not intervals:
            return 0
        
        # initialise current available rooms to empty array
        available_rooms = []
        
        # sort the meeting intervals based on start time
        intervals.sort(key=lambda x: x[0])

        # push 1st meeting end time to heap
        heapq.heappush(available_rooms, intervals[0][1])

        for meeting in intervals[1:]:
            # if current meeting start time is greater than end time of current meeting in heap
            # then remove end time from heap
            if available_rooms[0] <= meeting[0]:
                heapq.heappop(available_rooms)
            
            # add current meeting end time in heap
            heapq.heappush(available_rooms, meeting[1])
        
        # number of end times in heap is number of rooms required
        return len(available_rooms)
