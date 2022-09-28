class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        a = [i + 1 for i in range(n)]
        cur = 0
        l = n
        ans = -1
        for i in range(n):
            cur = (cur + k - 1) % l
            ans = a[cur]
            a = a[:cur] + a[cur + 1:] # Math is hard to think, but simulation is quick and easy.
            l -= 1
        return ans