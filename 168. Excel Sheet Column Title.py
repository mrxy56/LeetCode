class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        d = [chr(i) for i in range(ord('A'), ord('Z') + 1)] # Z is 26, so must use 0-25
        ans = []
        while columnNumber:
            ans.append(d[(columnNumber - 1) % 26])
            columnNumber = (columnNumber - 1) // 26 # Minus one to fit into 0-25
        return "".join(reversed(ans))