class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        flag = True
        l = len(intervals)
        for i in range(1, l):
            if intervals[i][0] < intervals[i - 1][1]:
                flag = False
                break
        if not flag:
            return False
        return True
            