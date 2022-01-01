# Left leaves
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, ls, mode):
            if node == None:
                return
            if node.left == None and node.right == None and mode == 'l':
                ls.append(node.val)
                return
            dfs(node.left, ls, 'l')
            dfs(node.right, ls, 'r')
        ans = 0
        ls = []
        dfs(root, ls, 'r')
        for num in ls:
            ans += num
        return ans