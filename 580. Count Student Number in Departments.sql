# Write your MySQL query statement below
# 1. Use RIGHT JOIN here since we want to keep the department even if it has 0.
# 2. Count s.stuent_id not * because we do not want NULL record.
SELECT d.dept_name AS dept_name, COUNT(s.student_id) AS student_number
FROM Student s RIGHT JOIN Department d ON s.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY student_number DESC, d.dept_name ASC
;
