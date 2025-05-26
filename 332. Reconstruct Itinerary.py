# 1. We need to find one itinerary, not all, so no backtracking.
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        a = {}
        m = len(tickets)
        for tik in tickets:
            f, t = tik[0], tik[1]
            if f in a:
                a[f].append(t)
            else:
                a[f] = [t]
        for k, v in a.items():
            v.sort()
        ls = []
        def dfs(cur):
            if cur in a:
                dests = a[cur]
                while dests:
                    dest = dests.pop(0)
                    dfs(dest)
            ls.append(cur)

        dfs("JFK")
        return ls[::-1]