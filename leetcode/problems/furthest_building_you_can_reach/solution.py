class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        jump_lengths = []
        n = len(heights)
        start, end = 0, n - 1

        # make a list of all the jumps required and sort in descending order based on jump length
        for idx in range(n - 1):
            jump = heights[idx + 1] - heights[idx]
            if jump <= 0:
                continue
            jump_lengths.append((jump, idx + 1))
        jump_lengths.sort()

        def isReachable(position, bricks, ladders):
            for jump in jump_lengths:
                jump_length, building_index = jump[0], jump[1]
                
                # if current mid building index is less than the comparing building index which means this building is on right side of our mid building
                # then ignore that building as we want to check if our mid building is reachable from left
                if building_index > position:
                    continue
                
                if jump_length <= bricks:
                    # use bricks first
                    bricks -= jump_length
                elif ladders >= 1:
                    # once bricks are over then use ladders
                    ladders -= 1
                else:
                    # if none of bricks or ladders is left that means we cannot reach this building
                    return False
            return True
        
        while start < end:
            # specific formula to get exact mid if length is odd and higher mid if length is even
            mid = start + (end - start + 1) // 2
            if isReachable(mid, bricks, ladders):
                # if current building is reachable then search for next reachable on right side
                start = mid
            else:
                # if current building is not reachable then search for previous reachable on left side
                end = mid - 1
        
        return end

        