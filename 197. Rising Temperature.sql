# Write your MySQL query statement below
# 1. Key is the function TO_DAYS.
# 2. The way to join two forms is also worth learning.
SELECT T1.id
FROM Weather T1 JOIN Weather T2
ON TO_DAYS(T1.recordDate) = TO_DAYS(T2.recordDate) + 1
WHERE T1.temperature > T2.temperature
