class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        d = defaultdict(bool)
        def hasZero(n):
            while n:
                if n % 10 == 0:
                    return True
                n = n // 10
            return False
        for i in range(0, n + 1):
            if hasZero(i):
                d[i] = True
            else:
                d[i] = False
        ans = []
        for i in range(1, n):
            x = i
            y = n - i
            if not d[x] and not d[y]:
                ans.append([x, y])
        return ans[0]