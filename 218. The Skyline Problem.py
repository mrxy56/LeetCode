# 1. Sweep Line + Priority Queue, only consider if highest left edge changes.
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        edges = []
        for i, building in enumerate(buildings):
            edges.append([building[0], i])
            edges.append([building[1], i])
        edges.sort()       
        live, ans = [], []
        idx = 0
        while idx < len(edges):
            cur_x = edges[idx][0]
            while idx < len(edges) and edges[idx][0] == cur_x:
                b = edges[idx][1]
                if buildings[b][0] == cur_x:
                    r = buildings[b][1]
                    h = buildings[b][2]
                    heapq.heappush(live, [-h, r])
                while live and live[0][1] <= cur_x:
                    heapq.heappop(live)
                idx += 1
            max_height = -live[0][0] if live else 0
            if not ans or max_height != ans[-1][1]:
                ans.append([cur_x, max_height])
        return ans
