# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.flag = 0
        def varify(root, subRoot):
            if not root and not subRoot:
                return True
            if not root and subRoot or root and not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            
            if not varify(root.left, subRoot.left):
                return False
            if not varify(root.right, subRoot.right):
                return False
            return True
            
        def findroot(root, subRoot):
            v = subRoot.val
            if root.val == v:
                if varify(root, subRoot):
                    self.flag = 1 # self.flag is important, we need a global variable to record
                    return 

            if root.left:
                findroot(root.left, subRoot)
            if root.right:
                findroot(root.right, subRoot)
            return 
         
        findroot(root, subRoot)
        if self.flag:
            return True
        else:
            return False