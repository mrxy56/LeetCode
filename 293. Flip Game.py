class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        n = len(currentState)
        if n <= 1:
            return []
        ans = []
        for i in range(n - 1):
            if currentState[i] == '+' and currentState[i] == currentState[i + 1]:
                tmp = deepcopy(currentState)
                tmp = list(tmp)
                tmp[i] = '-'
                tmp[i + 1] = '-'
                ans.append("".join(tmp))
        return ans