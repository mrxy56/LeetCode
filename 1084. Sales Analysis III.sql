# Write your MySQL query statement below
# 1. Use DISTINCT 
# 2. DATE should be quoted.
SELECT DISTINCT p.product_id, p.product_name
FROM Product p JOIN Sales s
ON p.product_id = s.product_id
WHERE p.product_id NOT IN (
    SELECT product_id
    FROM Sales
    WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31'
);