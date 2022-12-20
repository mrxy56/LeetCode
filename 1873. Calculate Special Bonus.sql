# Write your MySQL query statement below
# 1. ORDER BY is important
# 2. IF Statement: IF(... AND ..., True, False)
SELECT employee_id, IF(MOD(employee_id, 2) = 1 AND Left(name, 1) != 'M', salary, 0) AS bonus
FROM Employees
ORDER BY employee_id
;