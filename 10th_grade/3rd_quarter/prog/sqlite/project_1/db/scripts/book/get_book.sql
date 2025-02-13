SELECT
    book_id,
    locker,
    shelf
FROM
    books
WHERE
    (name LIKE '%' || ? || '%')
    AND (author LIKE '%' || ? || '%');
