class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        cur = 0
        for c in columnTitle:
            cur = cur * 26 + ord(c) - ord('A') + 1
        return cur