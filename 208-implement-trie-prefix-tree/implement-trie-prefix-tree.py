class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.is_leaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            i = ord(ch) - ord('a')
            if cur.child[i] == None:
                cur.child[i] = TrieNode()
            cur = cur.child[i]
        cur.is_leaf = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            i = ord(ch) - ord('a')
            if cur.child[i] == None:
                return False
            cur = cur.child[i]
        return cur.is_leaf

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            i = ord(ch) - ord('a')
            if cur.child[i] == None:
                return False
            cur = cur.child[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)