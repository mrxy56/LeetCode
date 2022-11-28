# Brute Force
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        maxyear = 1950
        minyear = 2050
        for log in logs:
            l, r = log
            r = r - 1
            if l < minyear:
                minyear = l
            if r > maxyear:
                maxyear = r
        maxcnt = 0
        ans = 1950
        for y in range(minyear, maxyear + 1):
            cnt = 0
            for log in logs:
                ll, rr = log
                if y >= ll and y < rr:
                    cnt += 1
            if cnt > maxcnt:
                maxcnt = cnt
                ans = y
        return ans