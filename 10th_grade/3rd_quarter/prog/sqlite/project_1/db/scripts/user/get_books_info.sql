SELECT
    b.book_id,
    b.name,
    b.author
FROM
    books AS b
    JOIN rents AS r ON b.book_id = r.book_id
WHERE
    r.user_id = ?;
