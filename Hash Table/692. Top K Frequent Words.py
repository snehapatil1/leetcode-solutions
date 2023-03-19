class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count_map = {}
        for word in words:
            if word not in word_count_map:
                word_count_map[word] = 0
            word_count_map[word] += 1
        
        count_word_map = {}
        for word in word_count_map:
            if word_count_map[word] not in count_word_map:
                count_word_map[word_count_map[word]] = []
            count_word_map[word_count_map[word]].append(word)
            count_word_map[word_count_map[word]].sort()

        count_word_map = dict(sorted(count_word_map.items(), reverse=True))

        op = []
        for key in count_word_map:
            for val in count_word_map[key]:
                if k > 0:
                    op.append(val)
                    k -= 1
        
        return op
