# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_index = 0
        def array_to_tree(left, right):
            if left > right:
                return None
            root_value = preorder[self.pre_index]
            root = TreeNode(root_value)
            self.pre_index += 1
            root.left = array_to_tree(left, in_index_mp[root_value] - 1)
            root.right = array_to_tree(in_index_mp[root_value] + 1, right)
            return root
        in_index_mp = {}
        for ind, v in enumerate(inorder):
            in_index_mp[v] = ind
        return array_to_tree(0, len(preorder) - 1)