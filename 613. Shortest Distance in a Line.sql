# Write your MySQL query statement below
# 1. Remember this grammar.
SELECT MIN(ABS(p1.x - p2.x)) as shortest
FROM
    Point p1 
    LEFT JOIN 
    Point p2 ON p1.x != p2.x