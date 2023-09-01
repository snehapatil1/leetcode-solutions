class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the array based on position and get lap time
        laps = [(target - psn)/spd for psn, spd in sorted(zip(position, speed))]
        cur, output = 0, 0

        # check for laptime from end since we want nearest car to the destination to be paired with other car
        # if lap time is > current time then this car can be clubbed with some other car
        for time in laps[::-1]:
            if time > cur:
                cur = time
                output += 1
        return output