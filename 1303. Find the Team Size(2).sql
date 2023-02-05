/* Write your T-SQL query statement below */
SELECT e1.employee_id AS employee_id, COUNT(e2.employee_id) AS team_size
FROM Employee e1 LEFT JOIN Employee e2
ON e1.team_id = e2.team_id
GROUP BY e1.employee_id