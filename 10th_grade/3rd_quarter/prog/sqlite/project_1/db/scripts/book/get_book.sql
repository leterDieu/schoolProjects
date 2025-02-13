SELECT
    book_id,
    case,
    shelf
FROM
    books
WHERE
    (name LIKE '%' || ? || '%')
    AND (author LIKE '%' || ? || '%');
