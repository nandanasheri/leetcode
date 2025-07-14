class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        
        curr.end = True

        

    def search(self, word: str) -> bool:

        def dfs(curr, j):
            for i in range(j, len(word)):
                if word[i] == ".":
                    for each in curr.children.values():
                        if dfs(each, i+1):
                            return True
                    # go through all possible values if none work, return False - don't return False immediately
                    return False
                    
                # iterative part traverse down a single path
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.end
        
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)