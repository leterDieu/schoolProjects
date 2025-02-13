SELECT
    u.user_id,
    u.name,
    u.lastname
FROM
    rents AS r
    JOIN users AS u ON r.user_id = u.user_id
WHERE
    book_id = ?;
