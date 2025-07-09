class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        start = self.root
        for i in word:
            if i not in start.children:
                start.children[i] = TrieNode()
            start = start.children[i]

        start.end = True

        # start = self.root

        # for i in word:
        #     print(start.children[i])

    def search(self, word: str) -> bool:
        start = self.root
        for i in word:
            if i not in start.children:
                return False
            start = start.children[i]

        return start.end

    def startsWith(self, prefix: str) -> bool:
        start = self.root
        for i in prefix:
            if i not in start.children:
                return False
            start = start.children[i]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)