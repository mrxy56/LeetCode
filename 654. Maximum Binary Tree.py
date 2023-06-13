# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:       
        def Max(arr):
            p = -1
            n = len(arr)
            if n == 0:
                return [-1, 0]
            val = arr[0]
            p = 0
            for i in range(n):
                if arr[i] > val:
                    val = arr[i]
                    p = i
            return [p, val]
        
        def dfs(nums):
            p, val = Max(nums)
            if p >= 0:
                node = TreeNode(val)
                node.left = dfs(nums[:p])
                node.right = dfs(nums[p + 1:])
                return node
            else:
                return None
        
        node = dfs(nums)
        return node