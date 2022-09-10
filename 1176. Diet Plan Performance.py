class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        l = len(calories)
        ans = 0
        s = [0 for i in range(l)]
        s[0] = calories[0]
        for i in range(1, l):
            s[i] = s[i - 1] + calories[i]
        for i in range(0, l - k + 1):
            if i == 0: # pay attention to i == 0
                sum = s[i + k - 1]
            else:
                sum = s[i + k - 1] - s[i - 1] 
            if sum < lower:
                ans -= 1
            if sum > upper:
                ans += 1
        return ans