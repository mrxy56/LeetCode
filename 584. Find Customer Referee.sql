# Write your MySQL query statement below
SELECT name
From Customer
WHERE referee_id <> 2 OR referee_id IS NULL 
;
# anything companed to NULL is unknown, so NULL should be processed. And use <>.