class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        a = [set() for i in range(n)]
        d = [0 for i in range(n)]
        for edge in edges:
            x, y = edge
            a[x].add(y)
            a[y].add(x)
            d[x] += 1
            d[y] += 1
        leaves = []
        for i in range(n):
            if d[i] == 1:
                leaves.append(i)
        remain = n
        while remain > 2:
            remain -= len(leaves)
            new_leaves = []
            while leaves: # like topological sort, find centroids, can be 1 or 2
                leaf = leaves.pop()
                x = a[leaf].pop()
                a[x].remove(leaf)
                if len(a[x]) == 1:
                    new_leaves.append(x)
            leaves = new_leaves
        return leaves