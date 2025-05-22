class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        s = '0000'
        S = set(deadends)
        D = [-1, 1]
        vis = set()
        if s in S:
            return -1
        q = [(s, 0)]
        vis.add(s)
        while q:
            ls, d = q.pop(0)
            if ls == target:
                return d
            ls = list(ls)
            for i in range(4):
                for dd in D:
                    l = deepcopy(ls)
                    n = (int(l[i]) + dd + 10) % 10
                    l[i] = str(n)
                    tmp = "".join(l)
                    if tmp not in vis and tmp not in S:
                        q.append((tmp, d + 1))
                        vis.add(tmp)
        return -1
                