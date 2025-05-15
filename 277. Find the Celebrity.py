# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# 1. Very interesting problem, find the candidate and verify it.
class Solution:
    def findCelebrity(self, n: int) -> int:
        c = 0
        for i in range(1, n):
            if knows(c, i):
                c = i
        for i in range(n):
            if c != i:
                if knows(c, i) or not knows(i, c):
                    return -1
        return c                    
                