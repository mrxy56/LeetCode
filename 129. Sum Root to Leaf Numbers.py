# Very easy.
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(node, last):
            if node == None:
                return
            if node.left == None and node.right == None:
                ans.append(last * 10 + node.val)
                return
            else:
                dfs(node.left, last * 10 + node.val)
                dfs(node.right, last * 10 + node.val)
        dfs(root, 0)
        return sum(ans)