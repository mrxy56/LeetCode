class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        ans = []
        for s in salary:
            if s == min_salary or s == max_salary:
                continue
            ans.append(s)
        return mean(ans)