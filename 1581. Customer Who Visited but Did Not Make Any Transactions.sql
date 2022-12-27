# Write your MySQL query statement below
# 1. NOT IN and GROUP BY.
SELECT customer_id, COUNT(*) AS count_no_trans
FROM Visits
WHERE visit_id NOT IN (
    SELECT DISTINCT visit_id
    FROM Transactions
)
GROUP BY customer_id
;