# Write your MySQL query statement below
SELECT P.project_id, E.employee_id
FROM Project as P
INNER JOIN Employee as E
ON E.employee_id = P.employee_id
WHERE (P.project_id, E.experience_years) in 
    (SELECT P.project_id, max(E.experience_years)
    FROM Project as P
    Inner Join Employee as E on E.employee_id = P.employee_id
    GROUP BY project_id)
;
 