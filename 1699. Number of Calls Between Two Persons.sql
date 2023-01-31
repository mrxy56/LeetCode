# UNION ALL
SELECT person1, person2, COUNT(*) AS call_count, SUM(duration) AS total_duration
FROM (SELECT from_id AS person1, to_id AS person2, duration
FROM Calls
WHERE from_id < to_id
UNION ALL
SELECT to_id AS person1, from_id AS person2, duration
FROM Calls
WHERE to_id < from_id) AS tmp
GROUP BY person1, person2