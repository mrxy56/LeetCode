# 1. Radix Sort.
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        class Node:
            def __init__(self, num, ind):
                self.num = num
                self.ind = ind
            def __lt__(self, other):
                if self.num != other.num:
                    return self.num < other.num
                return self.ind < other.ind
        N = []
        for i, num in enumerate(nums):
            N.append(Node(num, i))
        ls = []
        n = len(nums[0])
        for i in range(n - 1, -1, -1):
            N.sort(key = lambda x: x.num[i])
            ls.append(list(N))
        ans = []
        for q in queries:
            order, digits = q
            ans.append(ls[digits - 1][order - 1].ind)
        return ans