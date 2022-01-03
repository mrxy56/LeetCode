# The goal is to find the most popular circles, others will be invited only if the people in the circle are invited.
# Therefore, if i has favorite person f, f would has one indegree since we want to exclude less popular people first.
# Pay attention to the 2 people circle, assume them to be a couple, we can add all of this kind of groups.
# Then a big circle. Find the maximum of this two kinds.
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        def dfs(i, ls):
            f = favorite[i]
            favorite[i] = -1
            if f != -1:
                dfs(f, ls)
                ls.append(i)
            else:
                return
        n = len(favorite)
        indegrees = [0 for i in range(n)]
        out = [[] for i in range(n)]
        dp = [0 for i in range(n)]
        vis = [0 for i in range(n)]
        for i in range(n):
            f = favorite[i]
            indegrees[f] +=1
            out[i].append(f)
        from collections import deque
        q = deque()
        for i in range(n):
            if indegrees[i] == 0:
                q.append(i)
                vis[i] = 1
        while(q):
            t = q.pop()
            f = favorite[t]
            indegrees[f] -= 1
            dp[f] = max(dp[t] + 1, dp[f])
            if indegrees[f] == 0:
                q.append(f)
                vis[f] = 1
        pairs = 0
        ret = 0
        for i in range(n):
            if not vis[i]:
                length = 0
                cur = i
                while(vis[cur] == 0):
                    vis[cur] = 1
                    cur = favorite[cur]
                    length += 1
                if length == 2:
                    pairs += (2 + dp[i] + dp[favorite[i]])
                else:
                    ret = max(ret, length)
        return max(ret, pairs)