# Write your MySQL query statement below
SELECT project_id
FROM Project
GROUP BY project_id
HAVING count(employee_id) = (SELECT count(employee_id)
                            FROM Project
                            GROUP BY project_id
                            ORDER BY count(employee_id) DESC
                            LIMIT 1)
;
# Differences between HAVING and WHERE, HAVING is used in Group by.