# Write your MySQL query statement below
# 1. Use Having combined with GROUP BY.
# 2. If GROUP BY 2, do not use parentheses.
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING Count(timestamp) >= 3
;