# 1. Simulation, pay attention to the edge cases.
# 2. Must do two loops.
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import Counter
        mp = Counter(secret)
        bull = 0
        cow = 0
        for i, num in enumerate(guess):
            if guess[i] == secret[i]:
                bull += 1
                mp[guess[i]] -= 1
        for i, num in enumerate(guess):
            if guess[i] != secret[i] and guess[i] in mp and mp[guess[i]] > 0:
                mp[guess[i]] -= 1
                cow += 1
        return str(bull) + 'A' + str(cow) + 'B'