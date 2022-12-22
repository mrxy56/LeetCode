# Write your MySQL query statement below
# SELECT ON not SELECT WHERE
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p LEFT JOIN Address a
ON p.personId = a.personId
;