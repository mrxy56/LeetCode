# Write your MySQL query statement below
# 1. UNION.
# 2. LEFT join means we guarentee left.
# 3. RIGHT JOIN means we guarentee right.
SELECT e.employee_id
FROM Employees e 
LEFT JOIN Salaries s ON e.employee_id = s.employee_id
WHERE s.salary is NULL
UNION
SELECT s.employee_id
FROM Employees e 
RIGHT JOIN Salaries s ON e.employee_id = s.employee_id
WHERE e.name is NULL
ORDER BY employee_id
;
