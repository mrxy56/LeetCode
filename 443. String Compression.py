class Solution:
    def compress(self, chars: List[str]) -> int:
        group = [1]
        char = [chars[0]]
        for i in range(1, len(chars)): # This group operation is classical
            if chars[i] == chars[i - 1]:
                group[-1] += 1
            else:
                group.append(1)
                char.append(chars[i])
        ans = 0
        ls = ""
        for i, num in enumerate(group):
            ls += char[i]
            ls += "" if num == 1 else str(num)
            ans += 1
            if num == 1: # pay attention to edge case num == 1
                continue
            while num:
                ans += 1
                num = num // 10
        for i in range(ans):
            chars[i] = ls[i]
        return ans