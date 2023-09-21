# SELECT min(year) first then use LEFT JOIN
SELECT s1.product_id, s1.first_year, s2.quantity, s2.price
FROM (SELECT product_id, MIN(year) AS first_year
FROM Sales
GROUP BY product_id) s1 LEFT JOIN Sales s2
ON s1.product_id = s2.product_id AND s1.first_year = s2.year