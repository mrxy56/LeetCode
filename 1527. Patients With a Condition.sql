# Write your MySQL query statement below
# 1. Use like.
# 2. SELECT *
SELECT *
FROM Patients
WHERE conditions LIKE '% DIAB1%' OR conditions LIKE 'DIAB1%'
;
