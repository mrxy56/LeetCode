# 1. I was stuck at the beginning, but actually two loops can solve it.
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            tmp = 0
            for j in range(i, n):
                tmp += arr[j]
                if (j - i) % 2 == 0:
                    ans += tmp
        return ans