class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.value = 0
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, val):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True
        cur.value = val
        
    def search(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            else:
                cur = cur.children[ch]
        return cur.is_end
    
    def startsWith(self, prefix):
        self.ans = 0
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return 0
            else:
                cur = cur.children[ch]
        def dfs(cur):
            if cur.is_end:
                self.ans += cur.value
            for ch, node in cur.children.items():
                dfs(node)
        dfs(cur)
        return self.ans
    
class MapSum:

    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.startsWith(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)