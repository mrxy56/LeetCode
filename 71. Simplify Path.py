# 1. Simulation, quite straightforward, use queue.
class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        print(paths)
        ans = []
        for i, p in enumerate(paths):
            if p == '..':
                if len(ans):
                    ans.pop()
            elif p == '':
                continue
            elif p == '.':
                continue
            else:
                ans.append(p)
        s = "/".join(ans)
        if len(s) > 1 and s[-1] == '/':
            l = len(s)
            return '/' + s[:l - 1]
        else:
            return '/' + s