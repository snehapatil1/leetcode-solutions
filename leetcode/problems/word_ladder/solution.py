class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        graph = defaultdict(list)

        for word in wordList:
            for idx in range(len(word)):
                pattern = word[:idx] + "*" + word[idx + 1:]
                graph[pattern].append(word)
        
        visit = set()
        visit.add(beginWord)
        queue = deque([beginWord])
        pathLen = 1

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return pathLen
                for idx in range(len(word)):
                    pattern = word[:idx] + "*" + word[idx + 1:]
                    for w in graph[pattern]:
                        if w not in visit:
                            visit.add(w)
                            queue.append(w)
            pathLen += 1
        
        return 0