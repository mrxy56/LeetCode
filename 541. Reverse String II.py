class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ns = ""
        s = '#' + s # Add one '#' before
        l = len(s)
        mode = 1
        for i in range(1, l, k):
            if mode == 1:
                ns += s[i + k - 1: i - 1: -1]
            else:
                ns += s[i: i + k]
            mode = 1 - mode
        return ns