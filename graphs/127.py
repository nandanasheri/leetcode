class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adj_map = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = list(word)
                pattern[i] = "*"
                adj_map["".join(pattern)].append(word)
        
        queue = deque()
        queue.append((beginWord, 1))
        visited = set()

        while queue:
            currword, num = queue.popleft()
            visited.add(currword)
            if currword == endWord:
                return num
            for i in range(len(currword)):
                pattern = list(currword)
                pattern[i] = "*"
                for nei in adj_map["".join(pattern)]:
                    if nei not in visited:
                        queue.append((nei, num+1))

        return 0
        
        
        