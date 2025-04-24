# 1. Two pointers, pay attention that cnt can be greater than n, when the last element is 0.
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        cnt = 0
        for i in range(n):
            if arr[i] == 0:
                cnt += 2
            else:
                cnt += 1
            if cnt >= n:
                break
        j = n - 1
        if cnt > n:
            arr[j] = 0
            j -= 1
            i -= 1
        for k in range(i, -1, -1):
            if arr[k] == 0:
                arr[j] = arr[j - 1] = 0
                j -= 2
            else:
                arr[j] = arr[k]
                j -= 1
            