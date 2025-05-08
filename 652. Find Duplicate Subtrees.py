# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. Instead of using preorder and inorder, it uses triplelet to represent a subtree.

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        mp = {}
        
        def preorder(node):
            if node is None:
                seq1.append('N')
                return
            seq1.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
            return
        
        def inorder(node):
            if node is None:
                seq2.append('N')
                return
            inorder(node.left)
            seq2.append(str(node.val))
            inorder(node.right)
            return
        
        cur = root
        q = []
        q.append(cur)
        while q:
            node = q.pop()
            seq1 = []
            seq2 = []
            preorder(node)
            inorder(node)
            key = (".".join(seq1), ".".join(seq2))
            if key in mp:
                mp[key].append(node)
            else:
                mp[key] = [node]
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        ans = []
        for k, v in mp.items():
            if len(v) >= 2:
                ans.append(v[0])
        return ans
            
            