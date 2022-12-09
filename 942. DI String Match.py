# 1. Unique construction problem, when we meet 'I' we assign the loweset possible number so any number after it would cause an increcement.
# 2. Update the l and h to avoid repeated use of numbers.
class Solution(object):
    def diStringMatch(self, S):
        l, h = 0, len(S)
        ans = []
        for ch in S:
            if ch == 'I':
                ans.append(l)
                l += 1
            else:
                ans.append(h)
                h -= 1
        return ans + [l]