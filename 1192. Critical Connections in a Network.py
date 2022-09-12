class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.timer = 0
        low = [0 for i in range(n)]
        timeV = [0 for i in range(n)]
        visited = [False for i in range(n)]
        graph = defaultdict(list)
        ans = []
        def tarjan(start, pre): # Get familiar with Tarjan
            visited[start] = True
            timeV[start] = low[start] = self.timer
            self.timer += 1
            for neighbor in graph[start]:
                if neighbor == pre: continue
                if visited[neighbor]:
                    low[start] = min(low[start], timeV[neighbor])
                else:
                    tarjan(neighbor, start)
                    low[start] = min(low[start], low[neighbor])
                    if low[neighbor] > timeV[start]:
                        ans.append([start, neighbor])        

        l = len(connections)
        for i in range(l):
            x, y = connections[i][0], connections[i][1]
            graph[x].append(y)
            graph[y].append(x)

        tarjan(0, -1)
        
        return ans