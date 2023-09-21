# Use OR, first select those with 'Y' then those special employee_ids pre-selected.
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y' or employee_id IN (SELECT employee_id
FROM Employee
GROUP BY employee_id
HAVING COUNT(department_id) = 1)
