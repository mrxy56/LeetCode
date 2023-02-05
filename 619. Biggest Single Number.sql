/* Write your T-SQL query statement below */
SELECT ISNULL(
(SELECT num
FROM MyNumbers
GROUP BY num
HAVING COUNT(*) = 1
ORDER BY num DESC
OFFSET 0 ROWS FETCH FIRST 1 ROW ONLY), null) AS num