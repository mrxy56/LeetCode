class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mp = {}
        for string in strings:
            diff = ['0']
            for i, ch in enumerate(string):
                if i > 0:
                    diff.append(str((ord(string[i]) - ord(string[i - 1]) + 26) % 26))
            key = ".".join(diff)
            if key in mp:
                mp[key].append(string)
            else:
                mp[key] = [string]
        ans = []
        for k, v in mp.items():
            ans.append(v)
        return ans
                    