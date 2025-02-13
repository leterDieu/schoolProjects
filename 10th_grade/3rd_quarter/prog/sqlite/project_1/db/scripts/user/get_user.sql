SELECT
    user_id,
    ticker
FROM
    users
WHERE
    (name LIKE '%' || ? || '%')
    AND (lastname LIKE '%' || ? || '%');
