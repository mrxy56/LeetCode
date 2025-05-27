class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pre = [2 ** 31 - 1 for i in range(n)]
        cur = [2 ** 31 - 1 for i in range(n)]
        a = defaultdict(list)
        for flight in flights:
            s, t, c = flight
            a[s].append((s, t, c))
        q = []
        q.append(src)
        pre[src] = 0
        cur[src] = 0
        num = 1
        for i in range(k + 1):
            if len(q) == 0:
                break
            cnt = num
            num = 0
            for j in range(cnt):
                v = q.pop(0)
                for e in a[v]:
                    s, t, c = e
                    if cur[t] > pre[s] + c:
                        cur[t] = pre[s] + c
                        q.append(t)
                        num += 1
            pre = list(cur)
        return cur[dst] if cur[dst] < 2 ** 31 - 1 else -1