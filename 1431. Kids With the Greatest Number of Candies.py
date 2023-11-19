class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxc = max(candies)
        n = len(candies)
        ans = [False for i in range(n)]
        for i, candy in enumerate(candies):
            if candy + extraCandies >= maxc:
                ans[i] = True
        return ans
