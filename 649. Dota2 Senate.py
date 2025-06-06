# 1. It's wise to use two queues. Need to understand the meaning of the problem well.
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = []
        d = []
        n = len(senate)
        for i, s in enumerate(senate):
            if s == 'R':
                r.append(i)
            else:
                d.append(i)
        while r and d:
            r_ind = r.pop(0)
            d_ind = d.pop(0)
            if r_ind < d_ind:
                r.append(r_ind + n)
            else:
                d.append(d_ind + n)
        return "Radiant" if len(r) else "Dire"
            