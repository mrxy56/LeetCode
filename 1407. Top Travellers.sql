# Write your MySQL query statement below
# 1. IFNULL
# 2. LEFT JOIN
SELECT u.name, IFNULL(SUM(r.distance), 0) AS travelled_distance
FROM Users u LEFT JOIN Rides r
ON u.id = r.user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, name ASC