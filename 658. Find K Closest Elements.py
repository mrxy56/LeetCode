# 1. It is hard to solve it in binary search but easier to solve it in heap.
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        class Node:
            def __init__(self, val, ind):
                self.val = val
                self.ind = ind
    
            def __lt__(self, other):
                if abs(self.val - x) != abs(other.val - x):
                    return abs(self.val - x) < abs(other.val - x)
                else:
                    return self.ind < other.ind
        ls = []
        for i, a in enumerate(arr):
            ls.append(Node(a, i))
        heapq.heapify(ls)
        ans = []
        for i in range(k):
            v = heapq.heappop(ls)
            ans.append(v.val)
        ans.sort()
        return ans
        
        
        