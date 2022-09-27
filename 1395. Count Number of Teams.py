class Solution:
    def numTeams(self, rating: List[int]) -> int:
        l = len(rating)
        up = [0 for i in range(l)]
        down = [0 for i in range(l)]
        ans = 0
        for i in range(l):
            for j in range(i):
                if rating[i] < rating[j]: # this is interesting, you need a O(n^2) algorithm, so record those useful
                    up[i] += 1
                    ans += up[j]
                else:
                    down[i] += 1
                    ans += down[j]
        return ans