# Somehow, when I use buyer_id, it is incorrect, maybe because of duplicate names, use u.user_id instead.
SELECT u.user_id AS buyer_id, u.join_date AS join_date, COUNT(o.order_id) AS orders_in_2019
FROM Users u LEFT JOIN Orders o
ON u.user_id = o.buyer_id AND YEAR(o.order_date) = '2019'
GROUP BY u.user_id
ORDER BY u.user_id