SELECT
    p.name,
    t.title,
    t.premiered,
    r.rating
FROM
    titles AS t
    LEFT JOIN crew AS c ON t.title_id = c.title_id
    LEFT JOIN people AS p ON c.person_id = p.person_id
    LEFT JOIN rating AS r ON t.title_id = r.title_id
    LEFT JOIN film_types AS ft ON t.type = ft.id
WHERE
    p.name IN ('Tom Hanks', 'Julia Roberts', 'Natalie Portman')
    -- AND ft.film_type = 'movie'
ORDER BY
    r.rating DESC;
