# 1. Edge cases.
# 2. Need to break once find it.
# 3. Don't mix up i and j.
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n == 1 or n == 2:
            return False
        tmp1 = tmp2 = -1
        for i in range(1, n):
            if arr[i - 1] >= arr[i]:
                tmp1 = i - 1
                break
        for j in range(n - 2, -1, -1):
            if arr[j] <= arr[j + 1]:
                tmp2 = j + 1
                break
        if tmp1 != tmp2:
            return False
        return True