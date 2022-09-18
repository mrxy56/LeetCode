class Solution:
    def convert(self, s: str, numRows: int) -> str:
        a = [[] for i in range(numRows)]
        i = 0
        op = -1
        for c in s:
            a[i].append(c)
            if i == 0 or i == numRows - 1:
                op = op * (-1)            # Change direction once getting into edge, initializing as going up.
            if i + op >=0 and i + op < numRows:
                i = i + op                # Now index needs to be valid.
        ans = ""
        for x in range(numRows):
            for y in a[x]:
                ans += y
        return ans