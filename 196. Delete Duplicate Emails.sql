# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
# 1. Though for a two-record Table, we have 4 Records after JOIN but we only focus on ONE TABLE to delete.
DELETE p1 FROM Person p1, Person p2
WHERE 
    p1.Email = p2.Email AND p1.Id > p2.Id
;