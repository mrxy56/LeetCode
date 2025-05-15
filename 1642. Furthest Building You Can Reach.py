# 1. Firstly assign all the gaps as ladder and gradually regret by substituting the smallest gap with bricks, until reaching the limitation.
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        mp = {}
        d = []
        h = []
        cnt = 0
        for i in range(1, n):
            if heights[i] - heights[i - 1] > 0:
                d.append(heights[i] - heights[i - 1])
                mp[cnt] = i
                cnt += 1
        heapq.heapify(h)
        for i in range(ladders):
            if i >= len(d):
                break
            heapq.heappush(h, d[i])
        j = ladders
        flag = True
        while j < len(d):
            if len(h):
                v = h[0]
            else:
                if bricks >= d[j]:
                    bricks -= d[j]
                    j += 1
                    continue
                else:
                    flag = False
                    break
            if d[j] > v:
                if bricks >= v:
                    bricks -= v
                    heapq.heappop(h)
                    heapq.heappush(h, d[j])
                else:
                    flag = False
                    break
            else:
                if bricks >= d[j]:
                    bricks -= d[j]
                else:
                    flag = False
                    break
            j += 1
        if flag:
            return mp[j + 1] - 1 if j + 1 < len(d) else n - 1
        else:
            return mp[j] - 1 if j < len(d) else n - 1
        