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
        
    def replace(self, word):
        prefix = ""
        cur = self.root
        for ch in word:
            prefix = prefix + ch
            if ch not in cur.children:
                return word
            else:
                cur = cur.children[ch]
                if cur.is_end:
                    return prefix
        return word
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for d in dictionary:
            trie.insert(d)
        words = sentence.split()
        for i, word in enumerate(words):
            words[i] = trie.replace(word)
        return " ".join(words)