SELECT
    c.first_name,
    c.last_name,
    SUM(i.subtotal) AS subtotal_sum
FROM
    customer AS c
    LEFT JOIN invoice AS i ON c.customer_id = i.customer_id
GROUP BY
    c.customer_id
ORDER BY
    subtotal_sum DESC;
