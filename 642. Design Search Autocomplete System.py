# 1. Note that some words like 'a' can both be a word and a prefix. And if an input ends with '#', it should be inserted.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.times = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, times):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True
        cur.times += times
        
    def search(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return (False, 0)
            else:
                cur = cur.children[ch]
        return (cur.is_end, cur.times)
    
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
                ans.append((s, cur.times))
            for ch, childnode in cur.children.items():
                dfs(childnode, s + ch)
        dfs(cur, prefix)
        return ans   
    
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.s = ""
        for i, sentence in enumerate(sentences):
            self.trie.insert(sentence, times[i])

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.insert(self.s, 1)
        self.s = self.s + c
        ret = self.trie.startsWith(self.s)
        ret.sort(key = lambda x: (-x[1], x[0]))
        ans = []
        k = min(3, len(ret))
        for i in range(k):
            ans.append(ret[i][0])
        if c == "#":
            self.s = ""
        return ans


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)