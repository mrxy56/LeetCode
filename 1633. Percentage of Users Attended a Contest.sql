# Use subquery to calculate distinct users.
# Write your MySQL query statement below
SELECT r.contest_id, ROUND(COUNT(r.user_id)/(SELECT COUNT(user_id) FROM Users) * 100, 2) AS percentage
FROM Register r LEFT JOIN Users u
ON r.user_id = u.user_id
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC