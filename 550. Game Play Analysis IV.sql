# USE DATE_ADD instead of + 1
# SELECT MIN(event_date) first, making it easier for the next steps
SELECT ROUND(COUNT(a2.player_id)/COUNT(a1.player_id), 2) AS fraction
FROM (SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id) a1 LEFT JOIN Activity a2
ON a1.player_id = a2.player_id AND DATE_ADD(first_login, Interval 1 DAY) = a2.event_date