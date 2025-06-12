# Write your MySQL query statement below
/** Pay attention to the use of the Window Function and With. **/
WITH T AS
(SELECT employee_id, name, rating, review_date, row_num
FROM (SELECT e.employee_id, name, review_date, rating, ROW_NUMBER() OVER (PARTITION BY e.employee_id ORDER BY review_date DESC) AS row_num, COUNT(*) OVER (PARTITION BY e.employee_id) AS cnt
FROM employees e LEFT JOIN performance_reviews p
ON e.employee_id = p.employee_id) AS tmp
WHERE cnt >= 3 AND row_num <= 3)
SELECT t1.employee_id, t1.name, (t1.rating - t3.rating) AS improvement_score
FROM T t1, T t2, T t3
WHERE t1.row_num = 1 AND t2.row_num = 2 AND t3.row_num = 3
AND t1.employee_id = t2.employee_id AND t1.employee_id = t3.employee_id
AND t1.rating > t2.rating AND t2.rating > t3.rating
ORDER BY (t1.rating - t3.rating) DESC, name ASC
;
