class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right, boats = 0, len(people) - 1, 0
        people.sort()

        while left <= right:
            if people[right] == limit:
                boats += 1
                right -= 1
                continue
            weight = people[left] + people[right]
            if weight <= limit:
                boats += 1
                left += 1
                right -= 1
            else:
                boats += 1
                right -= 1
        
        return boats