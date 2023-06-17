# 1. Easy to miss the i == j case. No matter what, there should be one more boat.
# 2. At most two people in one boat.
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        if n == 1:
            return 1
        people.sort()
        i = 0
        j = n - 1
        ans = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            ans += 1
        return ans