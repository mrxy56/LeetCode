# Write your MySQL query statement below
-- Use MIN(course_id).
-- WHERE (a, b) IN is the key.
SELECT student_id, MIN(course_id) AS course_id, grade
FROM Enrollments
WHERE (student_id, grade) IN
(
    SELECT student_id, MAX(grade)
    FROM Enrollments
    GROUP BY student_id
)
GROUP BY student_id
ORDER BY student_id ASC