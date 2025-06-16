class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            hmap[tuple(count)].append(word)

        return list(hmap.values())

        # hmap = {}
        # output = []

        # for word in strs:
        #     sorted_word = "".join(sorted(word))
        #     if sorted_word not in hmap:
        #         hmap[sorted_word] = []
        #     hmap[sorted_word].append(word)
        
        # for key in hmap:
        #     output.append(hmap[key])

        # return output