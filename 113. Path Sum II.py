# You cannot use path.append(root.val) in the function directly since it will change the path itself, though I do not know why.
# Maybe it is because path is actually a pointer in the function paremeters.
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, targetSum, path):
            if root == None:
                return
            if targetSum - root.val == 0 and root.left == None and root.right == None:
                paths.append(path + [root.val])
                return
            dfs(root.left, targetSum - root.val, path + [root.val])
            dfs(root.right, targetSum - root.val, path + [root.val])
        paths = []
        dfs(root, targetSum, [])
        return paths
            