class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        i = 0
        j = len(haystack)
        while i + l - 1 < j:
            if needle == haystack[i: i + l]:
                return i
            i += 1
        return -1