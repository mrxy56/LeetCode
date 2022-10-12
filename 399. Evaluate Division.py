class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        w = {}
        
        def find(n_id):
            if n_id not in w:
                w[n_id] = (n_id, 1)
            g_id, n_w = w[n_id]
            if g_id != n_id:
                new_g_id, g_w = find(g_id)
                w[n_id] = (new_g_id, n_w * g_w) # Finally the father should be weight 1. When use find, update the weights.
            return w[n_id]
        
        def union(x, y, v):
            x_gid, x_w = find(x)
            y_gid, y_w = find(y)
            if x_gid != y_gid:
                w[x_gid] = (y_gid, y_w * v / x_w) # Different group has different weight, pay attention to the inflation.
                
        for (x, y), v in zip(equations, values):
            union(x, y, v)
                
        results = []
        for (x, y) in queries:
            if x not in w or y not in w:
                results.append(-1.0)
            else:
                x_gid, x_w = find(x)
                y_gid, y_w = find(y)
                if x_gid != y_gid:
                    results.append(-1.0)
                else:
                    results.append(x_w / y_w)
        return results