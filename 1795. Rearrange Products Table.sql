# Write your MySQL query statement below
# 1. UNION combine the result of multiple select.
# 2. Pay attention to the difference between String and number in this case.
SELECT product_id, 'store1' AS store, store1 AS price
FROM Products WHERE store1 is not NULL
UNION
SELECT product_id, 'store2' AS store, store2 AS price
FROM Products WHERE store2 is not NULL
UNION
SELECT product_id, 'store3' AS store, store3 AS price
FROM Products WHERE store3 is not NULL