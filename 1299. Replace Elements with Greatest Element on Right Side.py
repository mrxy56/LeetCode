# 1. Maintain the greatest value from the right to the left.
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxnum = arr[-1]
        n = len(arr)
        for i in range(n - 1, -1, -1):
            tmp = maxnum
            if arr[i] > maxnum:
                maxnum = arr[i]
            arr[i] = tmp
        arr[-1] = -1
        return arr