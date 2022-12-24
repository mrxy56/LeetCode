# Write your MySQL query statement below
# CASE (WHEN THEN) ELSE END
SELECT id,
    CASE
        WHEN tree.id = (SELECT t.id From Tree t WHERE t.p_id IS NULL)
            THEN 'Root'
        WHEN tree.id IN (SELECT t.p_id From Tree t)
            THEN 'Inner'
        ELSE 'Leaf'
    END AS type
From Tree
ORDER BY id
;