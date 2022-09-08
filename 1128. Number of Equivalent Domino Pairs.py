# A better solution is HashMap
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        l = len(dominoes)
        for i in range(l):
            if dominoes[i][0] > dominoes[i][1]:
                dominoes[i][0], dominoes[i][1] = dominoes[i][1], dominoes[i][0]
        dominoes.sort()
        i = 0
        j = 0
        ans = 0
        while i <= l and j <= l:
            if j == l:
                ans += (j - i) * (j - i - 1) / 2
                break
            if eq(dominoes[i], dominoes[j]):
                j += 1
            else:
                ans += (j - i) * (j - i - 1) / 2
                i = j
        return int(ans)