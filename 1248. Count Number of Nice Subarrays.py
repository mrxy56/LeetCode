# Kind of like two sum, first check itself and then its counterpart.
# Use flag to record how many numbers we have for each sum number.
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        sums = [0 for i in range(len(nums) + 1)]
        flag = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                sums[i] = sums[i - 1] + 1
            else:
                sums[i] = sums[i - 1]
            flag[sums[i]] += 1
        for i in range(len(nums)):
            if sums[i] == k:
                ans += 1
            if sums[i] >= k:
                ans += flag[sums[i] - k]
        return ans
                