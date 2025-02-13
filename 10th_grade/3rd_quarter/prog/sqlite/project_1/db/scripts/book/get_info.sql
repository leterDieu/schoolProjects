SELECT
    name,
    author,
    year,
    edition
FROM
    books
WHERE
    book_id = ?;
