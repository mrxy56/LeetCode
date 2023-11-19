# Write your MySQL query statement below
# 1. Mark the table in the main query as c, refer to it in the subquery.
# 2. DATE_ADD and DATE_SUB, BETWEEN...AND...
SELECT visited_on,
(
    SELECT SUM(amount)
    FROM Customer
    WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on
) AS amount,
ROUND(
    (
        SELECT SUM(amount) / 7
        FROM Customer
        WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on
    ), 
    2
) AS average_amount
FROM Customer c
WHERE visited_on >= (
    SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY)
    FROM customer
)
GROUP BY visited_on