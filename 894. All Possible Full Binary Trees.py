# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1. Each time we return a list of candadate trees.
# 2. Create a new subtree v each time.
# 3. Guarentee there is at least one node in left and right both.
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(num, depth):
            if num == 1:
                return [TreeNode(0)]
            ans = []
            for i in range(1, num - 1):
                j = num - 1 - i
                l = dfs(i, depth + 1)
                r = dfs(j, depth + 1)
                for ll in l:
                    for rr in r:
                        v = TreeNode(0)
                        v.left = ll
                        v.right = rr 
                        ans.append(v)
            return ans
        return dfs(n, 0)