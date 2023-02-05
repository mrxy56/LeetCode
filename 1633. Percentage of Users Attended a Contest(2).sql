/* Write your T-SQL query statement below */
-- Neets to pay specific attention to the ROUND part. You need to multiply it by 1.0 to make it a double.
SELECT r.contest_id, ROUND(COUNT(DISTINCT(r.user_id)) * 1.0 / (SELECT COUNT(user_id) FROM Users) * 100, 2) AS percentage 
FROM Register r, Users u
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC