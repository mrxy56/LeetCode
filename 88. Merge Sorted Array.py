# 1. Index is hard to calculate.
# 2. Merge sort, three pointers.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for t in range(m + n - 1, n - 1, -1):
            nums1[t] = nums1[t - n]
        i = n
        j = 0
        k = 0
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        if n == 0:
            return

        while i < m + n and j < n:
            if nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i += 1
                k += 1
            else:
                nums1[k] = nums2[j]
                j += 1
                k += 1

        while i < m + n and k < m + n:
            nums1[k] = nums1[i]
            i += 1
            k += 1

        while j < n and k < m + n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
        return