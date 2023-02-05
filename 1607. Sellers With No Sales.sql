/* Write your T-SQL query statement below */
SELECT seller_name
FROM Seller
WHERE seller_id NOT IN(
SELECT seller_id
FROM Orders
WHERE FORMAT(sale_date, 'yyyy') = '2020')
ORDER BY seller_name ASC
;