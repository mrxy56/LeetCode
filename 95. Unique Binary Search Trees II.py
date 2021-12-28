# Preorder traversal, using DFS, very clever way of constructing trees.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(start, end):
            if start > end:
                return [None]
            Ts = []
            for i in range(start, end + 1):
                lT = dfs(start, i - 1)
                rT = dfs(i + 1, end)
                for l in lT:
                    for r in rT:
                        nT = TreeNode(i)
                        nT.left = l
                        nT.right = r
                        Ts.append(nT)
            return Ts
        return dfs(1, n)