# first, calculate the inorder of the tree, second, find the two nodes that are in the wrong order, third, recover the tree.
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(r):
            if r == None:
                return []
            return inorder(r.left) + [r.val] + inorder(r.right)
        def find_two_swapped(nums):
            ordered_nums = sorted(nums)
            n = len(nums)
            for i in range(n):
                if ordered_nums[i] != nums[i]:
                    return ordered_nums[i], nums[i]
            
        def recover(r):
            if r:
                if r.val == x or r.val == y:
                    if r.val == x:
                        r.val = y
                    else:
                        r.val = x
                recover(r.left)
                recover(r.right)
        nums = inorder(root)
        print(nums)
        x, y = find_two_swapped(nums)
        recover(root)
        