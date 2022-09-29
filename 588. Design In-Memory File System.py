class TrieNode:
    def __init__(self):
        self.content = ""
        self.children = collections.defaultdict(TrieNode) # A Trie solution. Remember.
        self.isfile = False
        
class FileSystem:

    def __init__(self):
        self.top = TrieNode()

    def ls(self, path: str) -> List[str]:
        path_lst = path.split("/")
        node = self.top
        for p in path_lst:
            if not p:
                continue
            if node.children:
                node = node.children.get(p)
        if node.isfile:
            return [p]
        ans = [i for i in node.children.keys()]
        if not ans:
            return ans
        ans.sort()
        return ans

    def mkdir(self, path: str) -> None:
        path_lst = path.split("/")
        node = self.top
        for p in path_lst:
            if not p:
                continue
            node = node.children[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_lst = filePath.split("/")
        node = self.top
        for p in path_lst:
            if not p:
                continue
            node = node.children[p]
        node.content += content
        node.isfile = True

    def readContentFromFile(self, filePath: str) -> str:
        path_lst = filePath.split("/")
        node = self.top
        for p in path_lst:
            if not p:
                continue
            node = node.children.get(p)
        return node.content