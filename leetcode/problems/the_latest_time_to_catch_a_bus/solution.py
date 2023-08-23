class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        cur = 0
        
        for bus in buses:
            cap = capacity
            while cur < len(passengers) and passengers[cur] <= bus and cap > 0:
                cur += 1
                cap -= 1
            
        bus = buses[-1]
        last = bus if cap > 0 else passengers[cur - 1]
        passengers = set(passengers)
        while last in passengers:
            last -= 1
        return last