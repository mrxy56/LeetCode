"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# 1. The key is building a one-one map between the new and old nodes.

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        vis = set()
        mp = {}
        def dfs(node, new_node):
            for neighbor in node.neighbors:
                if (node.val, neighbor.val) not in vis:
                    vis.add((node.val, neighbor.val))
                    vis.add((neighbor.val, node.val))
                    if neighbor.val not in mp:
                        new_neighbor = Node(neighbor.val)
                        mp[neighbor.val] = new_neighbor
                    else:
                        new_neighbor = mp[neighbor.val]
                    new_node.neighbors.append(new_neighbor)
                    new_neighbor.neighbors.append(new_node)
                    dfs(neighbor, new_neighbor) 
        root = Node(node.val)
        mp[node.val] = root
        dfs(node, root)
        return root
        