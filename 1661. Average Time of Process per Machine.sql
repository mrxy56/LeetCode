# Write your MySQL query statement below
SELECT tmp.machine_id, ROUND(AVG(tmp.a2t - tmp.a1t), 3) AS processing_time
FROM (SELECT a1.machine_id, a1.process_id, a1.timestamp AS a1t, a2.timestamp AS a2t
FROM Activity a1 LEFT JOIN Activity a2
ON a1.machine_id = a2.machine_id AND a1.process_id = a2.process_id
WHERE a1.activity_type = 'start' AND a2.activity_type = 'end') AS tmp
GROUP BY machine_id