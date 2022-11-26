class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        n = len(accounts)
        for i in range(n):
            m = len(accounts[i])
            tmp = 0
            for j in range(m):
                tmp += accounts[i][j]
                if tmp > ans:
                    ans = tmp
        return ans