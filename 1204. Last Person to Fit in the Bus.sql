# It is wise to create two columns and group by the first column, then pick the largest one.
SELECT q1.person_name
FROM Queue q1 LEFT JOIN Queue q2
ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1