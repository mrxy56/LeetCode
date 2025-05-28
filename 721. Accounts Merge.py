# 1. Union Find, need to do the find for all the emails again in the end.
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        pa = {}
        r = {}
        mp = {}
        def find(x):
            if x == pa[x]:
                return x
            pa[x] = find(pa[x])
            return pa[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            if r[px] < r[py]:
                pa[px] = py
            elif r[px] > r[py]:
                pa[py] = px
            else:
                pa[px] = py
                r[py] += 1
                
        for account in accounts:
            n = len(account)
            for i in range(1, n):
                if account[i] not in pa:
                    pa[account[i]] = account[i]
                    r[account[i]] = 0
                    mp[account[i]] = account[0]
    
        for account in accounts:
            n = len(account)
            for i in range(1, n - 1):
                union(account[i], account[i + 1])
        
        for account in accounts:
            n = len(account)
            for i in range(1, n):
                find(account[i])
                
        ans = {}
        for email in pa:
            if pa[email] not in ans:
                ans[pa[email]] = [email]
            else:
                ans[pa[email]].append(email)
        ret = []
        for k, v in ans.items():
            v.sort()
            ls = [mp[v[0]]]
            for vv in v:
                ls.append(vv)
            ret.append(ls)
        return ret
        