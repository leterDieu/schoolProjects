CREATE VIEW v4 AS
SELECT
    *,
    ROW_NUMBER() OVER (
        ORDER BY
            p.price
    )
FROM
    orders AS o
    JOIN users AS u ON o.user_id = u.user_id
    JOIN products AS p ON o.product_id = p.product_id;
