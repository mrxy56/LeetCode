class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        ns = s + s
        if ns.find(goal) != -1:
            return True
        return False