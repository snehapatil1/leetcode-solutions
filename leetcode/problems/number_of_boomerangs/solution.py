class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        output = 0

        for x1, y1 in points:
            hash_map = defaultdict(int)
            for x2, y2 in points:
                # calculate distance from point 1 to point 2
                distance = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
                if distance in hash_map:
                    # if distance is already present in hashmap that means we have found other similar distance
                    # points so we increment output with twice of counter since both points j and k can be placed as
                    # [i, j, k] and [i, k, j] meaning 2 different combinations hence multiply by 2
                    # and increment counter by 1
                    output += hash_map[distance] * 2
                    hash_map[distance] += 1
                else:
                    # if distance is not present in hashmap then set the counter to 1 
                    # means only 1 point with this distance is encountered
                    hash_map[distance] = 1
        return output