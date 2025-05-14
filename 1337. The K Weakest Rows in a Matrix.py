class Node:
    def __init__(self, v):
        self.x, self.y = v[0], v[1]
    
    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ls = []
        for i, row in enumerate(mat):
            tmp = 0
            for x in row:
                if x == 1:
                    tmp += 1
            ls.append(Node((tmp, i)))
        heapq.heapify(ls)
        ans = []
        for i in range(k):
            v = heapq.heappop(ls)
            x, y = v.x, v.y
            ans.append(y)
        return ans
        
                    