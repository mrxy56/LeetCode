class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = defaultdict(int)
        max_number = 0
        for num in nums:
            d[num] += num
            max_number = max(max_number, num)
        
        dp = [0 for i in range(max_number + 1)]
        dp[1] = d[1]
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2] + d[i]) # if we want to do dp, we need to take it in order. We make decisions.
        return dp[max_number]