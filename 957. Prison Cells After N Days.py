class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        l = len(cells)
        prev, curr = cells, [0 for i in range(l)]
        d = {}
        a = {}
        d[0] = deepcopy(prev)
        a[str(prev)] = 0
        for r in range(1, n + 1):
            curr[0] = curr[l - 1] = 0
            for i in range(1, l - 1):
                if prev[i - 1] == prev[i + 1]:
                    curr[i] = 1
                else:
                    curr[i] = 0
            d[r] = deepcopy(curr) # Must use deepcopy, or else it is reference
            if a.get(str(curr)):
                ind = a[str(curr)]
                return d[(n - ind) % (r - ind) + ind] # Pay attention to the way of calculating index
            a[str(curr)] = r # list cannot be the key
            for i in range(l):
                prev[i] = curr[i]
        return curr