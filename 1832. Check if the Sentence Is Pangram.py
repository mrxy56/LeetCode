class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count = [0 for i in range(26)]
        for ch in sentence:
            count[ord(ch) - ord('a')] += 1
        for i in range(26):
            if count[i] == 0:
                return False
        return True
        