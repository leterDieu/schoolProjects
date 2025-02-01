SELECT
    t.title,
    t.premiered
FROM
    titles AS t
    LEFT JOIN crew AS c ON t.title_id = c.title_id
    LEFT JOIN people AS p ON c.person_id = p.person_id
    LEFT JOIN film_types AS ft ON t.type = ft.id
WHERE
    p.name = 'Tom Hanks'
    -- AND ft.film_type = 'movie'
ORDER BY
    t.premiered DESC;
