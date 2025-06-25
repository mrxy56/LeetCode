class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n = len(v1)
        m = len(v2)
        i = 0
        while i < n and i < m:
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1
            else:
                i += 1
        while i < n:
            if int(v1[i]) > 0:
                return 1
            else:
                i += 1
        while i < m:
            if int(v2[i]) > 0:
                return -1
            else:
                i += 1
        return 0