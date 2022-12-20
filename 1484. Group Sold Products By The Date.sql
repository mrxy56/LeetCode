# Write your MySQL query statement below
SELECT sell_date, COUNT(DISTINCT product) AS num_sold, 
GROUP_CONCAT(DISTINCT product ORDER BY product ASC SEPARATOR ',') AS products               
from Activities  
group by sell_date
order by sell_date