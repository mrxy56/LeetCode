class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        sorted_asteroids = sorted(asteroids)
        num = len(asteroids)
        for a in sorted_asteroids:
            if mass >= a:
                num -= 1
                mass += a
        if num == 0:
            return True
        return False
                