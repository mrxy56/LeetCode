/* Write your T-SQL query statement below */
-- 1. rating * 1.0 to make it a float.
-- 2. remember SUM(case when rating < 3 then 1 else 0 end).
SELECT query_name, ROUND(SUM(rating * 1.0 / position) / COUNT(*), 2) AS quality,
ROUND(SUM(case when rating < 3 then 1 else 0 end) * 1.0 / COUNT(*) * 100, 2)
AS poor_query_percentage
FROM Queries
GROUP BY query_name 
