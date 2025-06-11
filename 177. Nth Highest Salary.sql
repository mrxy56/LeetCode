/*
  1. Pay attention to declare.
  2. And unique.
*/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
    SET M = N - 1;
  RETURN (
      # Write your MySQL query statement below.
    SELECT DISTINCT salary AS getNthHighestSalary
    FROM Employee
    ORDER BY salary DESC
    LIMIT M, 1
  );
END