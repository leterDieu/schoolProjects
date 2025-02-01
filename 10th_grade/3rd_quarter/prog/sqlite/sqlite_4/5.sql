SELECT
    t.title,
    ft.film_type,
    gt.genre_name
FROM
    titles AS t
    LEFT JOIN film_types AS ft ON t.type = ft.id
    LEFT JOIN rating AS r ON t.title_id = r.title_id
    LEFT JOIN film_genres AS fg ON t.title_id = fg.title_id
    LEFT JOIN genre_types AS gt ON fg.genre_id = gt.id
WHERE
    r.votes > 100000
    AND r.rating > 8
GROUP BY
    ft.film_type,
    gt.genre_name;
