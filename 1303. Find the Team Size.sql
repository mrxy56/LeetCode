# Write your MySQL query statement below
SELECT employee_id, Count(team_id) OVER (PARTITION BY team_id) AS team_size
FROM Employee
;