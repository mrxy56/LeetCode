# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node, string):
            if node is None:
                return string + "N,"
            string += str(node.val) + ','
            string = helper(node.left, string)
            string = helper(node.right, string)
            return string
        return helper(root, "")
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(l):
            if l[0] == 'N':
                l.pop(0)
                return None
            node = TreeNode(l[0])
            l.pop(0)
            node.left = helper(l)
            node.right = helper(l)
            return node
        data = data.split(',')
        root = helper(data)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))