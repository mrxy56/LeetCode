# Write your MySQL query statement below
# 1. It is easy to write the outer query but it is harder to seperate the different department.
# 2. So, we need to use the variable outside to filter the query results and find the least salary from the top three.
# 3. Cannot use IN for some reason.

SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e LEFT JOIN Department d
ON e.departmentId = d.id
WHERE Salary >= (
    SELECT Salary
    FROM (
        SELECT DISTINCT salary AS Salary
        FROM Employee
        WHERE departmentId = e.departmentId
        ORDER BY Salary DESC
        LIMIT 3 OFFSET 0
    ) AS tmp
    ORDER BY Salary ASC
    LIMIT 0, 1
);