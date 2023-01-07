class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        n = len(command)
        for i in range(n):
            if command[i] == 'G':
                ans.append('G')
            elif i + 1 < n and command[i:i + 2] == '()':
                ans.append('o')
            elif i + 3 < n and command[i:i + 4] == '(al)':
                ans.append('al')
        return "".join(ans)