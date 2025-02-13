SELECT
    user_id,
    ticker
FROM
    users
WHERE
    (name LIKE '%' || ? || '%')
    OR (lastname LIKE '%' || ? || '%');
