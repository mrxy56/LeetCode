# Write your MySQL query statement below
SELECT email
from Person
group by email # group by and having count is worth noticing.
having count(email) > 1
;