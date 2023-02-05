/* Write your T-SQL query statement below */
-- CASE WHEN () THEN () ELSE () END
SELECT FORMAT(trans_date, 'yyyy-MM') AS month, country, COUNT(*) AS trans_count,
SUM(CASE WHEN STATE = 'APPROVED' THEN 1 ELSE 0 END) AS approved_count, SUM(amount) AS trans_total_amount,  SUM(CASE WHEN STATE = 'APPROVED' THEN AMOUNT ELSE 0 END) AS approved_total_amount 
FROM Transactions
GROUP BY FORMAT(trans_date, 'yyyy-MM'), country

