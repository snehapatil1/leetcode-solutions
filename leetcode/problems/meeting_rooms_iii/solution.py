class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        availableRooms = [i for i in range(n)]
        occupiedRooms = []
        roomCounter = [0] * n
        heapify(availableRooms)
        meetings.sort()

        for start_time, end_time in meetings:
            while occupiedRooms and occupiedRooms[0][0] <= start_time:
                end, room = heapq.heappop(occupiedRooms)
                heapq.heappush(availableRooms, room)

            if availableRooms:
                room = heapq.heappop(availableRooms)
                heapq.heappush(occupiedRooms, (end_time, room))
            else:
                cend, room = heapq.heappop(occupiedRooms)
                nend = cend + end_time - start_time
                heapq.heappush(occupiedRooms, (nend, room))
            
            roomCounter[room] += 1

        return roomCounter.index(max(roomCounter))