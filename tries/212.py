class TrieNode:
    def __init__ (self):
        self.children = {}
        self.word = False

class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = PrefixTrie()
        m = len(board)
        n = len(board[0])
        result = set()
        visited = set()

        # build out prefix trie
        for i in words:
            trie.insert(i)
        
        def dfs(i, j, node, word):
            if i >= m or j >= n or i < 0 or j < 0 or (i,j) in visited or board[i][j] not in node.children:
                return 
            visited.add((i,j))
            word += board[i][j]
            node = node.children[board[i][j]]
            if node.word:
                result.add(word)
            dfs(i,j+1,node,word)
            dfs(i+1,j,node,word)
            dfs(i-1,j,node,word)
            dfs(i,j-1,node,word)
            visited.remove((i,j))
        

        for i in range(m):
            for j in range(n):
                dfs(i,j, trie.root, "")
        
        return list(result)
        