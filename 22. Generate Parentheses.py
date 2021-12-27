# Classical recursion, first try to reach 3 '('s, then fill ')'s until it catches up '('s. 
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def cal(S, left, right):
            if left + right == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                cal(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(")")
                cal(S, left, right + 1)
                S.pop()           
        cal([], 0, 0)
        return ans