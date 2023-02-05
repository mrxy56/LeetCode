/* Write your T-SQL query statement below */
-- Use SELECT COUNT(*) FROM Delivery rather than COUNT(*) since COUNT(*) is the selected number of records.
SELECT ROUND(COUNT(order_date) * 1.0 / (SELECT COUNT(*) FROM Delivery) * 100, 2) AS immediate_percentage
FROM Delivery
WHERE order_date = customer_pref_delivery_date