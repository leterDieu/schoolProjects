SELECT
    t.title,
    GROUP_CONCAT (gt.genre_name),
    r.rating
FROM
    titles AS t
    LEFT JOIN film_types AS ft ON t.type = ft.id
    LEFT JOIN rating AS r ON t.title_id = r.title_id
    LEFT JOIN film_genres AS fg ON t.title_id = fg.title_id
    LEFT JOIN genre_types AS gt ON fg.genre_id = gt.id
WHERE
    r.votes > 100000
    -- AND ft.film_type = 'movie'
GROUP BY
    t.title
HAVING
    LENGTH (GROUP_CONCAT (gt.genre_name)) - LENGTH (GROUP_CONCAT (gt.genre_name, '')) = 1
ORDER BY
    r.rating DESC
LIMIT
    10;
