/* Write your T-SQL query statement below */
SELECT a.sale_date, a.sold_num - b.sold_num AS diff
FROM Sales a Left JOIN Sales b ON a.sale_date = b.sale_date and a.fruit!= b.fruit
WHERE a.fruit = 'apples'