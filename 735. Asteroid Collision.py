class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        l = len(asteroids)
        i = 0
        for i in range(l):
            while s and asteroids[i] < 0 and s[-1] > 0: # The difficult part of it is coding, it is wise to use while and else.
                if s[-1] < -asteroids[i]:
                    s.pop()
                    continue
                elif s[-1] == -asteroids[i]:
                    s.pop()
                break
            else:
                s.append(asteroids[i])
        return s