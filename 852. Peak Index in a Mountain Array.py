class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            if m > 0 and m < n - 1 and arr[m] > arr[m - 1] and arr[m] > arr[m + 1]:
                return m
            elif arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m - 1
