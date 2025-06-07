class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True
        
    def search(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            else:
                cur = cur.children[ch]
        return cur.is_end
    
    def startsWith(self, prefix):
        ans = []
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return ans
            else:
                cur = cur.children[ch]
        def dfs(cur, s):
            if cur.is_end:
                ans.append(s)
            for ch, childnode in cur.children.items():
                dfs(childnode, s + ch)
        dfs(cur, prefix)
        return ans

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        s = ""
        for i, product in enumerate(products):
            trie.insert(product)
        ans = []
        for ch in searchWord:
            s = s + ch
            ans.append(sorted(trie.startsWith(s))[:3])
        return ans
        